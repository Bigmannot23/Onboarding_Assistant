"""
Build an embedding index for the onboarding assistant knowledge base.

This script reads all Markdown files in the ``knowledge_base`` directory,
splits them into chunks, computes embeddings using OpenAI's embedding API,
and stores them in a FAISS index for efficient similarity search.

Before running this script, set the ``OPENAI_API_KEY`` environment
variable to your OpenAI API key.  You may need to install additional
dependencies (`faiss-cpu`, `openai`) listed in ``requirements.txt``.

Usage:

    python index_embeddings.py

This will create two files in the project root:
``kb_index.faiss`` and ``kb_docs.json``.  These files are consumed
by ``app.py`` at runtime.
"""

import json
import os
from pathlib import Path
from typing import List, Tuple

import faiss  # type: ignore
import numpy as np  # type: ignore
import openai  # type: ignore


def read_documents(folder: Path) -> List[Tuple[str, str]]:
    """Return a list of (doc_id, text) from all markdown files in folder."""
    docs = []
    for md in folder.glob("*.md"):
        with md.open() as f:
            text = f.read()
        docs.append((md.stem, text))
    return docs


def chunk_text(text: str, max_tokens: int = 200) -> List[str]:
    """Split long text into chunks of at most `max_tokens` words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunk = " ".join(words[i : i + max_tokens])
        chunks.append(chunk)
    return chunks


def embed_texts(texts: List[str]) -> np.ndarray:
    """Compute embeddings for a list of strings using OpenAI API."""
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable is not set")
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=texts,
    )
    embeds = [record["embedding"] for record in response["data"]]
    return np.array(embeds, dtype='float32')


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    kb_dir = base_dir / "knowledge_base"
    docs = read_documents(kb_dir)
    chunks = []
    metadata = []
    for doc_id, text in docs:
        for idx, chunk in enumerate(chunk_text(text)):
            chunks.append(chunk)
            metadata.append({"doc_id": doc_id, "chunk_index": idx, "text": chunk})
    # Compute embeddings in batches (OpenAI API supports up to 2048 inputs per request)
    embeddings = embed_texts(chunks)
    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    # Save index and metadata
    faiss.write_index(index, str(base_dir / "kb_index.faiss"))
    with (base_dir / "kb_docs.json").open("w") as f:
        json.dump(metadata, f)
    print(f"Indexed {len(chunks)} chunks from {len(docs)} documents.")


if __name__ == "__main__":
    main()