from app.agents.nodes.tool_router import tool_node


def test_tool_node_returns_scored_result() -> None:
    result = tool_node({"user_input": "hello tool"})
    assert result["route"] == "respond"
    assert "score=" in result["tool_result"]
