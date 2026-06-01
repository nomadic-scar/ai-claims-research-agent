from unittest.mock import MagicMock
from src.core.router import Router

def test_router_sends_claim_queries_to_research_agent():
    research = MagicMock()
    communication = MagicMock()
    workflow = MagicMock()

    research.handle.return_value = "research response"

    router = Router(research, communication, workflow)
    result = router.route("Why was claim 123 denied?")

    assert result == "research response"
    research.handle.assert_called_once()
    communication.handle.assert_not_called()
    workflow.handle.assert_not_called()


def test_router_sends_email_queries_to_communication_agent():
    research = MagicMock()
    communication = MagicMock()
    workflow = MagicMock()

    communication.handle.return_value = "communication response"

    router = Router(research, communication, workflow)
    result = router.route("Draft an email explaining the denial")

    assert result == "communication response"
    communication.handle.assert_called_once()
    research.handle.assert_not_called()
    workflow.handle.assert_not_called()


def test_router_sends_other_queries_to_workflow_agent():
    research = MagicMock()
    communication = MagicMock()
    workflow = MagicMock()

    workflow.handle.return_value = "workflow response"

    router = Router(research, communication, workflow)
    result = router.route("Create a checklist for onboarding")

    assert result == "workflow response"
    workflow.handle.assert_called_once()
    research.handle.assert_not_called()
    communication.handle.assert_not_called()
