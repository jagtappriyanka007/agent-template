from langchain_core.messages import HumanMessage, SystemMessage

from app.agents.state import AgentState
from app.core.llm_factory import get_chat_model


def responder_node(state: AgentState) -> AgentState:
    user_input = state.get("user_input", "")
    plan = state.get("plan", "")
    tool_result = state.get("tool_result")

    fallback_answer = (
        f"Response built with tool data: {tool_result}"
        if tool_result
        else f"Response for input: {user_input}"
    )

    try:
        llm = get_chat_model()
        context_bits = [f"User input: {user_input}"]
        if plan:
            context_bits.append(f"Plan: {plan}")
        if tool_result:
            context_bits.append(f"Tool result: {tool_result}")

        response = llm.invoke(
            [
                SystemMessage(
                    content=(
                        "You are an assistant that returns a concise, accurate final answer. "
                        "Use provided tool results when available."
                    )
                ),
                HumanMessage(content="\n".join(context_bits)),
            ]
        )
        answer = response.content if isinstance(response.content, str) else str(response.content)
    except Exception:
        answer = fallback_answer

    return {"final_answer": answer}
