from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from ..db import Base

class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, index=True)
    filename = Column(String)
    mimetype = Column(String)
    processed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
