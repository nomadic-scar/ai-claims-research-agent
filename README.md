# AI Claims Research Agent

A modular, multi‑agent system designed to analyze healthcare claims, explain benefit rules, draft communications, and automate operational workflows.  
Built with **Anthropic Claude**, **FastAPI**, and a clean, extensible architecture.

---

## 🚀 Features

### 🧠 Multi‑Agent Architecture
- **Research Agent** — interprets claim questions, generates SQL, and returns structured JSON.
- **Communication Agent** — drafts emails, explanations, and summaries in plain language.
- **Workflow Agent** — creates checklists, step‑by‑step processes, and operational workflows.

### 🔌 API Layer (FastAPI)
- `/query` endpoint routes requests to the correct agent.
- Typed request/response models using Pydantic.
- Easy to integrate with dashboards, UIs, or automation tools.

### 🗂 Clean Project Structure



