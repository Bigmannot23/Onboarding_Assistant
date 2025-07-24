# Onboarding Assistant

[![Build Status](https://img.shields.io/github/actions/workflow/status/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/onboarding_tests.yml?branch=main)](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/actions)

## 📈 Proof‑of‑ROI Quick Stats

An effective onboarding assistant accelerates ramp‑up time and reduces the burden on mentors.  When you deploy this assistant you can measure metrics such as:

- **Average onboarding time reduced:** `{{ insert percentage here }}` – the reduction in days or hours needed for a new hire or client to become productive.
- **FAQ resolution rate:** `{{ insert number here }}` – percentage of questions resolved by the assistant without human intervention.
- **Support hours saved:** `{{ insert hours here }}` – time saved by subject matter experts thanks to automated answers.

Track these metrics and include them in your portfolio’s proof‑of‑ROI section to demonstrate the tangible benefits of AI‑powered onboarding.

Empower new team members (or clients) with instant answers to
common questions.  This project uses vector search and large
language models to build a knowledge‑base Q&A tool—demonstrating how
to combine AI and data structures for practical support tasks.

## 🧠 What It Does

- Indexes your documentation: The `index_embeddings.py` script reads all
  Markdown files in the `knowledge_base` folder, splits them into chunks,
  generates embeddings via OpenAI, and stores them in a FAISS index.
- Answers questions: The Streamlit app (`app.py`) loads the FAISS index,
  retrieves the most relevant snippets for a given question, and uses
  ChatGPT to craft a helpful response.

## ⚙️ Setup

1. Add your own Markdown files to `knowledge_base/` to teach the
   assistant about your organization (handbooks, FAQs, processes).
2. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key.
3. Run `python index_embeddings.py` to build the index.  This will
   create `kb_index.faiss` and `kb_docs.json`.
4. Install dependencies and start the app:

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

5. Ask a question in the UI.  The assistant will return an answer
   drawn from your documentation along with the context snippets it used.

## 🔍 Why This Impresses

This project showcases the integration of vector search, prompt
engineering, and LLMs into a cohesive tool.  It demonstrates:

- **Data ingestion and indexing:** Reading and embedding documents.
- **Retrieval‑augmented generation:** Combining relevant snippets with an
  LLM to produce accurate answers.
- **User interface:** A polished Streamlit front end for interactive use.

## 🔐 Security & Privacy

All knowledge base documents stay local to your repository or hosting environment.  The assistant sends only the retrieved context and user’s question to the OpenAI API.  Do not include confidential information in your Markdown files unless you are hosting the assistant on a secured, private environment.  Store your `OPENAI_API_KEY` in environment variables or deployment secrets—never commit it to the repository.

## 🛠️ Configuration

The assistant’s behavior can be tuned using `config.yaml`:

```yaml
model: gpt-3.5-turbo      # which Chat model to use
temperature: 0.3          # controls creativity of responses
max_tokens: 500           # maximum length of answers
top_k: 4                  # number of retrieved chunks to feed into the prompt
embed_model: "text-embedding-ada-002"  # OpenAI embedding model
```

Feel free to adjust these parameters based on cost, latency, and answer quality considerations.  You can also switch to open‑source models hosted locally by modifying `index_embeddings.py` and `app.py`.

## 🧪 Unit Tests & Continuous Integration

A simple test suite lives in the `tests/` directory.  Tests verify that your knowledge base contains at least one document and that the configuration file is valid YAML.  Use `python -m unittest discover tests` to run them.  A GitHub Action (see `.github/workflows/onboarding_tests.yml`) runs these tests on each push and surfaces the result via the badge above.

Adding this repo to your portfolio proves that you can build
AI‑powered knowledge systems that scale onboarding and customer
support—valuable for companies of any size.