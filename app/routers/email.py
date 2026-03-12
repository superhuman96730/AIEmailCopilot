from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from ..services import nlp
from ..db import get_db
from sqlalchemy.orm import Session
from ..models.email import Email

router = APIRouter(prefix="/emails", tags=["emails"])


class EmailIn(BaseModel):
    sender: str
    subject: Optional[str] = None
    body: str


class EmailOut(BaseModel):
    id: int
    sender: str
    subject: Optional[str]
    category: str
    priority: str
    summary: str


class ReplyIn(BaseModel):
    body: str
    tone: Optional[str] = "neutral"


class ReplyOut(BaseModel):
    suggested_reply: str


@router.post("/classify", response_model=EmailOut)
def classify_email(email: EmailIn, db: Session = Depends(get_db)):
    result = nlp.classify_email(email.body)
    if not result:
        raise HTTPException(status_code=500, detail="Classification failed")

    # persist (simplified)
    db_email = Email(
        sender=email.sender,
        subject=email.subject,
        body=email.body,
        classified_as=result.get("category"),
        priority=result.get("priority"),
        summarized=result.get("summary"),
    )
    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return EmailOut(
        id=db_email.id,
        sender=db_email.sender,
        subject=db_email.subject,
        category=db_email.classified_as,
        priority=db_email.priority,
        summary=db_email.summarized,
    )


@router.post("/reply", response_model=ReplyOut)
def suggest_reply(req: ReplyIn):
    reply = nlp.generate_reply(req.body, tone=req.tone)
    if not reply:
        raise HTTPException(status_code=500, detail="Reply generation failed")
    return ReplyOut(suggested_reply=reply)
