from anthropic import Anthropic
import json

class ResearchAgent:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def handle(self, query):
        prompt = open("src/core/prompts/research_prompt.md").read()

        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=800,
            messages=[
                {"role": "user", "content": f"{prompt}\n\nQuery: {query}"}
            ]
        )

        return response.content[0].text
