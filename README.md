# AI Claims Research Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)


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

---

## 🧪 Mock Mode (No API Key Required)

This project includes a **Mock Mode** that allows anyone to run the system without:

- an Anthropic API key  
- a database  
- external dependencies  

Mock Mode returns **realistic fake outputs** for all three agents (Research, Communication, Workflow).  
This makes the project fully runnable for demos, interviews, and portfolio reviewers.

### Enable Mock Mode

Set the environment variable:
MOCK_MODE=true


Mock Mode returns realistic fake outputs for all three agents (Research, Communication, Workflow).  
This makes the project fully runnable for demos, interviews, and portfolio reviewers.


---

## 🛠️ Tech Stack

**Languages & Runtime**
- Python 3.10+

**AI & LLM**
- Anthropic Claude (Opus / Sonnet)

**Backend Framework**
- FastAPI  
- Pydantic (typed request/response models)

**Architecture**
- Modular multi-agent system  
- Router-based agent selection  
- Prompt templates stored in Markdown  
- Mock Mode for offline development

**Tooling**
- Uvicorn (local server)  
- Pytest (unit tests)  
- GitHub (version control)

---

## 🏗️ System Architecture

```mermaid
flowchart TD

    User[User Query] --> API[FastAPI /query Endpoint]

    API --> Router[Router]

    Router -->|Claim Question| ResearchAgent
    Router -->|Email Draft| CommunicationAgent
    Router -->|Workflow Request| WorkflowAgent

    ResearchAgent -->|Mock Mode| MockData1[(Fake Claim Data)]
    CommunicationAgent -->|Mock Mode| MockData2[(Fake Email)]
    WorkflowAgent -->|Mock Mode| MockData3[(Fake Checklist)]

    ResearchAgent -->|Real Mode| AnthropicAPI[(Anthropic Claude API)]
    CommunicationAgent -->|Real Mode| AnthropicAPI
    WorkflowAgent -->|Real Mode| AnthropicAPI

    Router --> Response[JSON Response]
