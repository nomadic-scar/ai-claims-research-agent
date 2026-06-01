from anthropic import Anthropic

class CommunicationAgent:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def handle(self, query):
        prompt = """
You are a communication agent. Your job is to:

1. Draft clear, professional messages.
2. Summarize claim findings.
3. Explain benefit rules in plain language.
4. Write outreach emails when asked.

Always return plain text. No JSON.
"""

        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=600,
            messages=[
                {"role": "user", "content": f"{prompt}\n\nTask: {query}"}
            ]
        )

        return response.content[0].text
