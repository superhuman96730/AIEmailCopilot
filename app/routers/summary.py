from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/summary", tags=["summary"])

class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str
    word_count: int

@router.post("/generate", response_model=SummaryResponse)
def generate_summary(req: SummaryRequest):
    words = len(req.text.split())
    return SummaryResponse(summary=req.text[:50], word_count=words)
