from src.core.utils import mock_mode

from anthropic import Anthropic

class CommunicationAgent:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def handle(self, query: str) -> str:
        # ---- MOCK MODE ----
        if mock_mode():
            return (
                "Hi team,\n\n"
                "This claim was denied due to missing prior authorization. "
                "Please submit the required documentation and resubmit the claim.\n\n"
                "Thanks,\nAI Assistant"
            )

        # ---- REAL MODE ----
        prompt = open("src/core/prompts/communication_prompt.md").read()

        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=600,
            messages=[
                {"role": "user", "content": f"{prompt}\n\nQuery: {query}"}
            ]
        )

        return response.content[0].text

