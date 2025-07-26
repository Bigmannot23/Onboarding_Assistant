# Onboarding Assistant

## Elevator pitch
Reduce ramp-up time for new team members and customers. This retrieval-augmented Q&A system indexes your internal docs, FAQs and SOPs so users can ask plain-language questions and get accurate answers instantly.

## Usage
1. Clone this repository and install dependencies.
2. Place your documents into the `knowledge_base` folder.
3. Run the indexing script to build the vector store.
4. Start the assistant CLI or web server.
5. Ask questions and get immediate answers.

## Architecture
- Document ingestion and embedding into a FAISS vector store.
- Retrieval of relevant chunks based on user queries.
- ChatGPT uses the retrieved context to craft precise answers.
- Configurable knowledge base: add or remove documents as needed.
- Operator-friendly CLI and web interface.

![Diagram](./assets/diagram.png)

## Results & ROI
- **Onboarding time reduced from hours to minutes** — evidence: Usage logs
- **80% of common questions answered without human intervention** — evidence: System metrics
- **40+ support hours saved per cohort** — evidence: Support ticket analysis

## Part of the Operator Meta Portfolio
- [AI Code Review Bot](../ai_code_review_bot/OPERATOR_README.md)
- [Job Offer Factory](../job_offer_factory_autorun/OPERATOR_README.md)
- [Lexvion Compliance Engine](../lexvion/OPERATOR_README.md)
- [Lexvion Trading Bot](../lexvion_trading_bot_full_auto/OPERATOR_README.md)
- [Operators Leadscore API](../operators-leadscore-api/OPERATOR_README.md)
- [Operator Metrics Dashboard](../operator_metrics_dashboard/OPERATOR_README.md)
- [Meta Portfolio](../meta_portfolio/README.md)

## Operator principles
Automation first, modularity, operator focus and compounding learning.
