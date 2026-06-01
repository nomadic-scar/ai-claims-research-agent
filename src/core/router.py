class Router:
    def __init__(self, research_agent, communication_agent, workflow_agent):
        self.research_agent = research_agent
        self.communication_agent = communication_agent
        self.workflow_agent = workflow_agent

    def route(self, query):
        q = query.lower()

        # Claims + benefit logic → Research Agent
        if "claim" in q or "benefit" in q:
            return self.research_agent.handle(query)

        # Drafting emails, explanations → Communication Agent
        if "email" in q or "draft" in q or "explain" in q:
            return self.communication_agent.handle(query)

        # Everything else → Workflow Agent
        return self.workflow_agent.handle(query)
