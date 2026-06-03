from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    user_input: str = Field(min_length=1)
    session_id: str | None = None


class AgentInvokeResponse(BaseModel):
    answer: str


class AgentChunk(BaseModel):
    delta: str
