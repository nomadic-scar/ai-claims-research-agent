from anthropic import Anthropic

class WorkflowAgent:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def handle(self, query):
        prompt = """
You are a workflow automation agent. Your responsibilities:

1. Break down multi-step operational tasks.
2. Generate checklists or step-by-step workflows.
3. Automate routine claims operations tasks.
4. Provide structured, actionable instructions.

Return clear text instructions. No JSON unless explicitly asked.
"""

        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=600,
            messages=[
                {"role": "user", "content": f"{prompt}\n\nTask: {query}"}
            ]
        )

        return response.content[0].text
