# AI Claims Research Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

A modular, multi‑agent system designed to analyze healthcare claims, explain benefit rules, draft communications, and automate operational workflows.  
Built with **Anthropic Claude**, **FastAPI**, and a clean, extensible architecture.

---

## 🎯 Project Goals

This project was built to:

- **Show real-world architecture** — not just a notebook, but a modular, multi-agent backend with routing, prompts, and an API.
- **Model healthcare operations** — reflect how claims, benefit rules, and workflows are actually handled in payer/PBM environments.
- **Demonstrate production thinking** — clean structure, clear separation of concerns, mock mode, and testability.
- **Create a portfolio-ready artifact** — something a hiring manager or engineer can open, understand, and run in minutes.

---

## 🧭 Why I Built This

I’ve spent years working in healthcare and PBM operations, where a lot of claim research is still manual, repetitive, and slow.  
I wanted to explore how modern LLMs could:

- interpret messy, real-world claim questions  
- reason over benefit rules and denial reasons  
- generate clear explanations and next steps for humans  

This project is my way of combining:

- **domain experience** in claims and prior auth  
- **technical skills** in Python, FastAPI, and LLMs  
- **system design** for multi-agent architectures  

It’s not just a toy—it’s a prototype of the kind of internal tool I wish more ops teams had.

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

## 🧩 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nomadic-scar/ai-claims-research-agent.git
cd ai-claims-research-agent
