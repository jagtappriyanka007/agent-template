from app.agents.nodes.planner import planner_node


def test_planner_node_sets_route() -> None:
    state = planner_node({"user_input": "use tool"})
    assert state["route"] == "tool"
