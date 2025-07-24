"""
Interactive onboarding assistant powered by OpenAI and FAISS.

This Streamlit app enables users to ask questions about your company's
knowledge base.  It retrieves relevant information from indexed documents
using vector similarity and generates a response with an LLM.  Use this
project to show how you can integrate large language models into
practical tools that scale onboarding and support.

To run locally:

    pip install -r requirements.txt
    streamlit run app.py

Before running, ensure that ``kb_index.faiss`` and ``kb_docs.json`` exist in
the project root.  Generate them by running ``python index_embeddings.py``
after setting your ``OPENAI_API_KEY`` environment variable.
"""

import json
import os
from pathlib import Path
from typing import List

import faiss  # type: ignore
import numpy as np  # type: ignore
import openai  # type: ignore
import streamlit as st  # type: ignore


def load_index(base_dir: Path):
    index = faiss.read_index(str(base_dir / "kb_index.faiss"))
    with (base_dir / "kb_docs.json").open() as f:
        metadata = json.load(f)
    return index, metadata


def embed_query(query: str) -> np.ndarray:
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable is not set")
    response = openai.Embedding.create(
        model="text-embedding-ada-002", input=[query]
    )
    vector = np.array(response["data"][0]["embedding"], dtype="float32")
    return vector


def search_similar_chunks(
    index: faiss.Index, metadata: List[dict], query_vector: np.ndarray, k: int = 3
) -> List[str]:
    D, I = index.search(query_vector.reshape(1, -1), k)
    # Flatten indices and gather texts
    results = []
    for idx in I[0]:
        results.append(metadata[idx]["text"])
    return results


def generate_answer(query: str, context: List[str]) -> str:
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    prompt = (
        "You are an onboarding assistant.  Use the following context to answer "
        "the user's question concisely and helpfully.\n\n"
    )
    context_text = "\n\n".join(context)
    prompt += f"Context:\n{context_text}\n\nQuestion: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.3,
    )
    return response.choices[0].message["content"].strip()


def main() -> None:
    st.set_page_config(page_title="Onboarding Assistant", layout="centered")
    st.title("🔎 Onboarding Assistant")
    st.markdown(
        "Ask any question about Lexvion Solutions and receive an answer "
        "based on our internal knowledge base.  This assistant demonstrates "
        "how AI and vector search can streamline onboarding and support."
    )

    base_dir = Path(__file__).resolve().parent
    try:
        index, metadata = load_index(base_dir)
    except Exception as e:
        st.error(
            "Error loading index.  Make sure to run `index_embeddings.py` "
            "and set your OPENAI_API_KEY."
        )
        st.stop()

    query = st.text_input("Enter your question:")
    if query:
        with st.spinner("Thinking..."):
            query_vector = embed_query(query)
            chunks = search_similar_chunks(index, metadata, query_vector)
            answer = generate_answer(query, chunks)
        st.markdown("### Answer")
        st.write(answer)
        with st.expander("Context snippets"):
            st.write(chunks)


if __name__ == "__main__":
    main()