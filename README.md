# Shopping Assistant (shopping-agent) ✅

**A small agent-based toolkit to research and compare products across e-commerce stores.**

Built with CrewAI and specialized scraping/search tools, this project automates finding product listings, extracting prices, shipping details, discounts, and recommending the best value.

---

## 🔍 Features

- Orchestrated agents for product research and analysis (e.g., `E-commerce Product Researcher`, `Deals & Benefits Analyst`).
- Integrations with search & scraping tools (`SerperDevTool`, `FirecrawlScrapeWebsiteTool`).
- Config-driven settings using `pydantic`/`pydantic-settings` and `.env` support.
- Example flow provided in `main.py` showing an end-to-end product comparison.

---

## ⚙️ Requirements

- Python 3.11 or newer
---

## 🚀 Installation

Prefer installing in a virtual environment:

```bash
uv init .
uv sync
```

---

## 🔐 Configuration

This project expects API keys to be provided via environment variables or a `.env` file (see `app/config/base.py`):

- `OPENAI_API_KEY` (OpenAI)
- `FIRECRAWL_API_KEY` (FireCrawl)
- `SERPER_API_KEY` (Serper.dev search)

Create a `.env` file at the project root:

```env
OPENAI_API_KEY=sk-...
FIRECRAWL_API_KEY=fc_...
SERPER_API_KEY=serper_...
```

> ⚠️ Keep these secrets out of version control.

---

## ▶️ Usage

A minimal example is provided in `main.py`. It sets up two agents (researcher and analyst), defines tasks, and runs a `Crew` to perform the workflow.

Run the example:

```bash
uv run main.py
```

The script will print a comparison result (the example searches for `Sony WH-1000XM5 Headphones`). Customize `product_name` or modify the agents and tasks in `main.py` to experiment.

---

## 🧪 Development

- Editing code: follow usual Git workflow on branch `feat/add-agent` (or create a new branch for features/fixes).
- No tests are included yet; add unit/integration tests as needed.
- Lint & format with your preferred tools (e.g., `ruff`, `black`).

---

## 🤝 Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a feature branch
3. Add tests and documentation for your changes
4. Open a pull request describing the change

---

## 📄 License

This repository includes a `LICENSE` file — see it for license terms.

---

## 📫 Contact

If you run into issues or have questions, open an issue in the repository: `aman-cc/shopping-agent`.

---

Happy shopping and researching! 🛍️
