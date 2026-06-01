FULL README.txt (Plain Text Version)
AI Claims Research Agent
Python 3.10+
FastAPI Backend
Anthropic Claude
MIT License
Project Status: Active
A modular, multi‑agent system designed to analyze healthcare claims, explain benefit rules, draft communications, and automate operational workflows. Built with Anthropic Claude, FastAPI, and a clean, extensible architecture.
---
PROJECT GOALS
This project was built to:
• Show real-world architecture — not just a notebook, but a modular, multi-agent backend with routing, prompts, and an API.
• Model healthcare operations — reflect how claims, benefit rules, and workflows are actually handled in payer/PBM environments.
• Demonstrate production thinking — clean structure, separation of concerns, mock mode, and testability.
• Create a portfolio-ready artifact — something a hiring manager or engineer can open, understand, and run in minutes.
---
WHY I BUILT THIS
I’ve spent years working in healthcare and PBM operations, where a lot of claim research is still manual, repetitive, and slow.
I wanted to explore how modern LLMs could:
• interpret messy, real-world claim questions
• reason over benefit rules and denial reasons
• generate clear explanations and next steps for humans
This project is my way of combining:
• domain experience in claims and prior auth
• technical skills in Python, FastAPI, and LLMs
• system design for multi-agent architectures
It’s not just a toy — it’s a prototype of the kind of internal tool I wish more ops teams had.
---
FEATURES
MULTI‑AGENT ARCHITECTURE
• Research Agent — interprets claim questions, generates SQL, and returns structured JSON.
• Communication Agent — drafts emails, explanations, and summaries in plain language.
• Workflow Agent — creates checklists, step‑by‑step processes, and operational workflows.
API LAYER (FASTAPI)
• /query endpoint routes requests to the correct agent.
• Typed request/response models using Pydantic.
• Easy to integrate with dashboards, UIs, or automation tools.
---
CLEAN PROJECT STRUCTURE
ai-claims-research-agent/
│
├── src/
│   ├── agents/
│   │   ├── research_agent.py
│   │   ├── communication_agent.py
│   │   └── workflow_agent.py
│   ├── router/
│   │   └── agent_router.py
│   ├── prompts/
│   │   ├── research_prompt.md
│   │   ├── communication_prompt.md
│   │   └── workflow_prompt.md
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   └── main.py
│
├── demo.py
├── requirements.txt
├── .env.example
└── README.md
---
HOW TO RUN LOCALLY
1. Clone the repository
git clone https://github.com/nomadic-scar/ai-claims-research-agent.git
cd ai-claims-research-agent
2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate
(Windows: .venv\Scripts\activate)
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
cp .env.example .env
Default:
MOCK_MODE=true
5. Run the FastAPI server
uvicorn src.main:app –reload
Docs: http://localhost:8000/docs
6. Run the terminal demo
python demo.py
---
MOCK MODE (NO API KEY REQUIRED)
Mock Mode allows anyone to run the system without:
• an Anthropic API key
• a database
• external dependencies
It returns realistic fake outputs for all three agents.
Enable Mock Mode:
MOCK_MODE=true
---
TECH STACK
Languages & Runtime
• Python 3.10+
AI & LLM
• Anthropic Claude (Opus / Sonnet)
Backend Framework
• FastAPI
• Pydantic
Architecture
• Modular multi-agent system
• Router-based agent selection
• Prompt templates stored in Markdown
• Mock Mode for offline development
Tooling
• Uvicorn
• Pytest
• GitHub
---
SYSTEM ARCHITECTURE (MERMAID DIAGRAM)
flowchart TD
User –> API
API –> Router
Router –> ResearchAgent
Router –> CommunicationAgent
Router –> WorkflowAgent
ResearchAgent –> MockData1
CommunicationAgent –> MockData2
WorkflowAgent –> MockData3
ResearchAgent –> AnthropicAPI
CommunicationAgent –> AnthropicAPI
WorkflowAgent –> AnthropicAPI
Router –> Response
---
FUTURE ENHANCEMENTS
• Database Integration
• Logging & Monitoring
• Agent Memory
• Frontend UI
• Docker Support
• Authentication
• Deployment
---
SCREENSHOTS (COMMENTED OUT IN MD VERSION)
---
LICENSE
MIT License — see LICENSE file for details.
