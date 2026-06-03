from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get(
    "/health",
    summary="Liveness probe",
    description="Basic liveness endpoint for container and orchestrator checks.",
)
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get(
    "/ready",
    summary="Readiness probe",
    description="Readiness endpoint to verify the service can receive traffic.",
)
async def ready() -> dict[str, str]:
    return {"status": "ready"}
