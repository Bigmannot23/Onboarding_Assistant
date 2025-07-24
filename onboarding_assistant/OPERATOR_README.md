# Operator Guide – Onboarding Assistant

This guide explains how to configure, run, and extend the **Onboarding Assistant**, a retrieval‑augmented question‑answering tool that helps new team members or clients get up to speed quickly.

## 🧰 Setup

1. **Prepare your knowledge base.**  Add Markdown files into the `knowledge_base/` directory.  Each file represents a source of knowledge—handbooks, FAQs, engineering principles, SOPs, and even your personal philosophy.
2. **Install dependencies.**  From `onboarding_assistant/` run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key.**  Define the `OPENAI_API_KEY` environment variable in your shell or your deployment secrets.  For example, on Linux/macOS:

   ```bash
   export OPENAI_API_KEY=sk-...
   ```

4. **Review configuration.**  Open `config.yaml` and adjust the model, temperature, token limits, number of retrieved chunks (`top_k`), and the embedding model.  Do not include your API key here.
5. **Index the documents.**  Run:

   ```bash
   python index_embeddings.py
   ```

   This will create `kb_index.faiss` and `kb_docs.json`, which the Streamlit app uses to answer questions.
6. **Launch the assistant.**  Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   Ask a question in the UI and the assistant will return an answer along with the context snippets.

## ⚙️ Configuration Options

`config.yaml` defines the parameters of both embedding and generation:

| Field | Purpose |
| --- | --- |
| `model` | Which Chat completion model to use for answering questions. |
| `temperature` | Controls randomness; lower is more deterministic. |
| `max_tokens` | Maximum token length of generated answers. |
| `top_k` | Number of top‑ranked chunks from the FAISS index to include in the prompt. |
| `embed_model` | The model used to create vector embeddings. |

Changing these parameters allows you to balance response quality, cost, and latency.  If you switch to a different embedding model, rebuild the index by rerunning `index_embeddings.py`.

## ▶️ How to Run & Test

- **Run Locally:** Follow the setup steps above.  Ensure `kb_index.faiss` and `kb_docs.json` exist; otherwise run `python index_embeddings.py`.
- **Run Unit Tests:** Execute:

  ```bash
  python -m unittest discover tests
  ```

  The tests verify that your knowledge base contains at least one file and that `config.yaml` is valid.

## 🔧 How to Extend or Fork

- **Add new documents:** Simply drop more `.md` files into `knowledge_base/`, rerun `index_embeddings.py`, and the assistant will incorporate them.
- **Use a different LLM provider:** Replace the OpenAI API calls in `index_embeddings.py` and `app.py` with calls to another provider (e.g. Anthropic, Cohere) or a local model.  Ensure that the embedding model you choose is compatible with FAISS.
- **Customize the UI:** Edit `app.py` to adjust the layout, style, or add new widgets (e.g. history of previous questions).
- **Feedback loops:** Add logging to record questions and ratings of the responses.  Use this data to continually improve your knowledge base and prompts.

## 🛠️ Troubleshooting Tips

| Problem | Solution |
| --- | --- |
| **`OPENAI_API_KEY` not found** | Set the environment variable or configure a secret in your deployment platform. |
| **Empty or irrelevant answers** | Ensure your knowledge base contains relevant documents and that `top_k` is not too low.  Increase `temperature` slightly if responses are too terse. |
| **`FileNotFoundError` for `kb_index.faiss`** | Run `python index_embeddings.py` after adding or editing documents. |
| **Slow response times** | Decrease `max_tokens` or switch to a smaller model.  Ensure your deployment has sufficient network bandwidth. |

Armed with this guide, you can deploy a robust onboarding assistant that captures your company’s institutional knowledge and scales your support capacity.