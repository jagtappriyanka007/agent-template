from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers.agent import router as agent_router
from app.api.routers.health import router as health_router
from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_logging()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description=(
            "Agentic AI API built with FastAPI, LangGraph, and LangChain. "
            "Use /docs for interactive docs and /openapi.json for the machine-readable spec."
        ),
        version="{{ cookiecutter.version }}",
        openapi_url="/openapi.json",
        redoc_url="/redoc",
        lifespan=lifespan,
        openapi_tags=[
            {"name": "health", "description": "Health and readiness probes."},
            {"name": "agent", "description": "Agent invoke and streaming endpoints."},
        ],
    )

    @app.get("/")
    async def root() -> dict[str, str]:
        return {"service": "{{ cookiecutter.project_slug }}", "status": "ok"}

    app.include_router(health_router)
    app.include_router(agent_router)
    return app


app = create_app()
