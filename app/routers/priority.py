from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..db import get_db

router = APIRouter(prefix="/priority", tags=["priority"])

class PriorityRequest(BaseModel):
    email_id: int

class PriorityResponse(BaseModel):
    email_id: int
    priority_level: str

@router.post("/detect", response_model=PriorityResponse)
def detect_priority(req: PriorityRequest, db: Session = Depends(get_db)):
    # placeholder logic
    return PriorityResponse(email_id=req.email_id, priority_level="normal")
