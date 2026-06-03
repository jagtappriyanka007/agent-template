from langchain_core.tools import tool


@tool
async def db_lookup_tool(key: str) -> str:
    if not key.strip():
        raise ValueError("key cannot be empty")
    return f"stub-db-result: {key}"
