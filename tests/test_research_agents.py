from unittest.mock import MagicMock
from src.agents.research_agent import ResearchAgent

def test_research_agent_handles_query():
    # Mock the Anthropic client
    mock_client = MagicMock()
    mock_client.messages.create.return_value.content = [
        MagicMock(text="mocked response")
    ]

    agent = ResearchAgent(api_key="test-key")
    agent.client = mock_client  # Inject mock

    result = agent.handle("Why was claim 123 denied?")
    assert result == "mocked response"
