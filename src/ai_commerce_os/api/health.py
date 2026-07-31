from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok"]


@router.get("/live", response_model=HealthResponse, include_in_schema=False)
async def liveness() -> HealthResponse:
    """Return success when the process can serve HTTP traffic."""
    return HealthResponse(status="ok")


@router.get("/ready", response_model=HealthResponse, include_in_schema=False)
async def readiness() -> HealthResponse:
    """Return success when application initialization is complete."""
    return HealthResponse(status="ok")
