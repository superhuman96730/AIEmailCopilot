from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/admin", tags=["admin"])

class AdminStats(BaseModel):
    total_users: int
    total_emails: int
    api_uptime: str

@router.get("/stats", response_model=AdminStats)
def get_admin_stats():
    return AdminStats(total_users=0, total_emails=0, api_uptime="99.9%")
