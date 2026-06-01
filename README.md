# AI Claims Research Agent

A multi-agent AI system built using the Claude API to automate claims research, benefit configuration lookup, SQL generation, and operational workflows. This project demonstrates how natural language queries can be converted into structured SQL, executed against adjudication and benefit configuration datasets, and returned as clean, actionable outputs.

---

## 🚀 Key Capabilities
- Natural-language → SQL generation  
- Automated claims research summaries  
- Multi-agent orchestration (research, communication, workflow)  
- Structured JSON outputs  
- Optional FastAPI server for integration  
- Clean, extensible architecture  

---

## 🧠 System Architecture

### Agents
- **Research Agent**  
  Converts natural language into SQL, executes queries, and returns structured results.

- **Communication Agent**  
  Drafts outreach messages, explanations, and summaries.

- **Workflow Agent**  
  Handles recurring tasks and multi-step operational flows.

### Router
Determines which agent should handle each incoming request.

---

## 📁 Repository Structure


