from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str

class ClaimResult(BaseModel):
    claim_id: Optional[int]
    status: Optional[str]
    denial_reason: Optional[str]
    benefit_rule: Optional[str]
    recommended_next_steps: Optional[List[str]]

class AgentResponse(BaseModel):
    agent: str
    output: str
