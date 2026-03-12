from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db import Base, get_db

# create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# override get_db dependency

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_classify_email():
    payload = {
        "sender": "user@example.com",
        "subject": "Hello",
        "body": "This is a test email body."
    }
    response = client.post("/emails/classify", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["sender"] == payload["sender"]
    assert data["category"] == "general"
    assert data["priority"] == "normal"
    assert "summary" in data


def test_suggest_reply():
    payload = {
        "body": "Can you provide more details about the project?",
        "tone": "friendly"
    }
    response = client.post("/emails/reply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "suggested_reply" in data
    assert "auto-generated" in data["suggested_reply"]
