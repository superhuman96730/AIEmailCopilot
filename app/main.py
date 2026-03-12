from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Email Copilot")

# create tables on startup
from .db import engine, Base


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# include routers
from .routers import email

app.include_router(email.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Email Copilot API"}
