from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])

class HealthStatus(BaseModel):
    status: str
    version: str = "1.0.0"

@router.get("/", response_model=HealthStatus)
def health_check():
    return HealthStatus(status="healthy")
