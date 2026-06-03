from langchain_core.tools import tool


@tool
async def search_tool(query: str) -> str:
    if not query.strip():
        raise ValueError("query cannot be empty")
    return f"stub-search-result: {query}"
