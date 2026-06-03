import pytest

from app.chains.tools.search_tool import search_tool


@pytest.mark.asyncio
async def test_search_tool_returns_stub() -> None:
    result = await search_tool.ainvoke({"query": "hello"})
    assert "stub-search-result" in result
