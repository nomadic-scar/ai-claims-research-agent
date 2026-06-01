from src.core.utils import mock_mode

from anthropic import Anthropic

class WorkflowAgent:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def handle(self, query: str) -> str:
        # ---- MOCK MODE ----
        if mock_mode():
            return (
                "- Verify member eligibility\n"
                "- Check benefit rule PA-001\n"
                "- Gather clinical documentation\n"
                "- Submit prior authorization\n"
                "- Resubmit claim\n"
            )

        # ---- REAL MODE ----
        prompt = open("src/core/prompts/workflow_prompt.md").read()

        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=600,
            messages=[
                {"role": "user", "content": f"{prompt}\n\nTask: {query}"}
            ]
        )

        return response.content[0].text

