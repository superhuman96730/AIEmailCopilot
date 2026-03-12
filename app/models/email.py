from sqlalchemy import Column, Integer, String, Text, Boolean
from ..db import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, index=True)
    subject = Column(String, index=True)
    body = Column(Text)
    classified_as = Column(String, index=True)
    priority = Column(String, index=True)
    summarized = Column(Text)
    created_at = Column(String)
