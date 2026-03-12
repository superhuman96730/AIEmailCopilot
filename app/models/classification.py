from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from ..db import Base

class ClassificationResult(Base):
    __tablename__ = "classification_results"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, index=True)
    model_used = Column(String, index=True)
    confidence = Column(Integer)
    result = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
