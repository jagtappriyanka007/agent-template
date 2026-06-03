from langgraph.graph import END, StateGraph

from app.agents.nodes.planner import planner_node
from app.agents.nodes.responder import responder_node
from app.agents.nodes.tool_router import tool_node
from app.agents.state import AgentState


def route_after_plan(state: AgentState) -> str:
    return state.get("route", "respond")


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("planner", planner_node)
    graph.add_node("tool", tool_node)
    graph.add_node("respond", responder_node)

    graph.set_entry_point("planner")
    graph.add_conditional_edges(
        "planner",
        route_after_plan,
        {
            "tool": "tool",
            "respond": "respond",
        },
    )
    graph.add_edge("tool", "respond")
    graph.add_edge("respond", END)
    return graph.compile()


compiled_graph = build_graph()
