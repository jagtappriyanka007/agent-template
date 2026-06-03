from collections.abc import AsyncIterator

import anyio

from app.agents.graph import compiled_graph
from app.api.schemas.agent import AgentChunk, AgentInvokeResponse, AgentRequest


async def invoke_agent(request: AgentRequest) -> AgentInvokeResponse:
    payload = {"user_input": request.user_input}
    if hasattr(compiled_graph, "ainvoke"):
        result = await compiled_graph.ainvoke(payload)
    else:
        result = await anyio.to_thread.run_sync(compiled_graph.invoke, payload)
    answer = result.get("final_answer", "")
    return AgentInvokeResponse(answer=answer)


async def stream_agent(request: AgentRequest) -> AsyncIterator[AgentChunk]:
    payload = {"user_input": request.user_input}

    if hasattr(compiled_graph, "astream"):
        async for update in compiled_graph.astream(payload, stream_mode="updates"):
            if not isinstance(update, dict):
                continue

            for _, node_update in update.items():
                if not isinstance(node_update, dict):
                    continue

                final_answer = node_update.get("final_answer")
                if not final_answer:
                    continue

                for token in str(final_answer).split():
                    yield AgentChunk(delta=token + " ")
        return

    result = await anyio.to_thread.run_sync(compiled_graph.invoke, payload)
    for token in str(result.get("final_answer", "")).split():
        yield AgentChunk(delta=token + " ")
