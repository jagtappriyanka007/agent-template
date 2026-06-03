# Cookiecutter: Agent Service Template

Generate a FastAPI + LangGraph + LangChain + Cython + Docker project:

```bash
cookiecutter ./cookiecutter-agent-service
```

This template includes:
- FastAPI API skeleton with invoke and SSE stream endpoints
- LangGraph state machine and nodes
- LangChain model factory via `init_chat_model`
- Cython module with Python fallback
- uv + Makefile workflow
- Dockerfile + docker-compose
