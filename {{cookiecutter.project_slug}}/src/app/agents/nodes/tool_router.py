from app.agents.state import AgentState
from app.cython_modules import CYTHON_ENABLED, score_sum


def tool_node(state: AgentState) -> AgentState:
    user_input = state.get("user_input", "")
    lengths = [float(len(token)) for token in user_input.split()] or [float(len(user_input))]
    score = score_sum(lengths)
    backend = "cython" if CYTHON_ENABLED else "python-fallback"
    return {
        "tool_result": f"{backend}-score={score:.2f}; input={user_input}",
        "route": "respond",
    }
