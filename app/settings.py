import os
from sqlalchemy.pool import StaticPool

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
API_TITLE = "AI Email Copilot API"
API_VERSION = "1.0.0"
