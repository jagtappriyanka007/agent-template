from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.api.schemas.agent import AgentChunk, AgentInvokeResponse, AgentRequest
from app.services.run_agent import invoke_agent, stream_agent

router = APIRouter(prefix="/v1/agent", tags=["agent"])


@router.post(
    "/invoke",
    response_model=AgentInvokeResponse,
    summary="Invoke agent once",
    description="Runs the LangGraph workflow and returns a single final response.",
)
async def invoke(request: AgentRequest) -> AgentInvokeResponse:
    return await invoke_agent(request)


@router.post(
    "/stream",
    summary="Stream agent response",
    description="Runs the LangGraph workflow and streams incremental SSE data chunks.",
)
async def stream(request: AgentRequest) -> StreamingResponse:
    async def event_stream():
        async for chunk in stream_agent(request):
            payload = AgentChunk(delta=chunk.delta)
            yield f"data: {payload.model_dump_json()}\\n\\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )
