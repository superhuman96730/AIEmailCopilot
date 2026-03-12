from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/stats", tags=["stats"])

class Stats(BaseModel):
    total_emails: int = 0
    classified: int = 0
    pending: int = 0

@router.get("/", response_model=Stats)
def get_stats():
    return Stats()
