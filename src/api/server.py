from fastapi import FastAPI
from src.api.models import QueryRequest, AgentResponse
from src.core.router import Router
from src.agents.research_agent import ResearchAgent
from src.agents.communication_agent import CommunicationAgent
from src.agents.workflow_agent import WorkflowAgent
import os

app = FastAPI(title="AI Claims Research Agent API")

# Initialize agents
api_key = os.getenv("ANTHROPIC_API_KEY")
research = ResearchAgent(api_key)
communication = CommunicationAgent(api_key)
workflow = WorkflowAgent(api_key)

# Initialize router
router = Router(research, communication, workflow)

@app.post("/query", response_model=AgentResponse)
def query_endpoint(request: QueryRequest):
    output = router.route(request.query)

    # Determine which agent responded
    agent = "unknown"
    q = request.query.lower()

    if "claim" in q or "benefit" in q:
        agent = "research"
    elif "email" in q or "draft" in q or "explain" in q:
        agent = "communication"
    else:
        agent = "workflow"

    return AgentResponse(agent=agent, output=output)
