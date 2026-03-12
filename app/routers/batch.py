from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/batch", tags=["batch"])

class BatchProcessRequest(BaseModel):
    email_ids: list

class BatchProcessResponse(BaseModel):
    processed: int
    failed: int

@router.post("/process", response_model=BatchProcessResponse)
def batch_process(req: BatchProcessRequest):
    return BatchProcessResponse(processed=len(req.email_ids), failed=0)
