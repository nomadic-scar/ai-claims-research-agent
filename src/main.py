from src.core.router import Router
from src.agents.research_agent import ResearchAgent
from src.agents.communication_agent import CommunicationAgent
from src.agents.workflow_agent import WorkflowAgent
import os

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")

    research = ResearchAgent(api_key)
    communication = CommunicationAgent(api_key)
    workflow = WorkflowAgent(api_key)

    router = Router(research, communication, workflow)

    while True:
        query = input("\nEnter a query: ")
        response = router.route(query)
        print("\nResponse:\n", response)

if __name__ == "__main__":
    main()
