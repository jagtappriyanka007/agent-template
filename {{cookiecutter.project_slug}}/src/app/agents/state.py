from typing import TypedDict


class AgentState(TypedDict, total=False):
    user_input: str
    plan: str
    route: str
    tool_result: str
    final_answer: str
