from langchain_core.messages import HumanMessage, SystemMessage

from app.agents.state import AgentState
from app.core.llm_factory import get_chat_model


def planner_node(state: AgentState) -> AgentState:
    text = state.get("user_input", "")
    route = "tool" if "tool" in text.lower() else "respond"

    plan = "basic-plan"
    try:
        llm = get_chat_model()
        response = llm.invoke(
            [
                SystemMessage(
                    content=(
                        "You are a planning assistant. Produce a short one-line plan "
                        "for answering the user request."
                    )
                ),
                HumanMessage(content=text),
            ]
        )
        plan = response.content if isinstance(response.content, str) else str(response.content)
    except Exception:
        plan = "basic-plan"

    return {"plan": plan, "route": route}
