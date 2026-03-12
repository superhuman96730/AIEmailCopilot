from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from ..db import Base

class ProcessingJob(Base):
    __tablename__ = "processing_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_type = Column(String)
    status = Column(String, default="pending")
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
