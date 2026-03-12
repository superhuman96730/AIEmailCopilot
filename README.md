# AI Email Copilot

A backend system designed to automatically classify, prioritize, and generate responses for incoming emails using NLP models. Demonstrates applied AI techniques in a scalable architecture.

## Features

- Automatically classify incoming emails
- Generate suggested replies
- Detect priority emails
- Summarize long messages

## Tech Stack

- Python
- HuggingFace Transformers
- FastAPI
- PostgreSQL
- Redis
- Gmail API
- Docker

## Architecture

Email → NLP Classifier → Priority Detection → AI Response Generator → API

## Development

1. Create a virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API: `uvicorn app.main:app --reload`

The `app.services.email_client` module contains stubs for interacting with email providers (e.g. via Gmail API).

### Running tests

```bash
pytest
```

### Using Docker Compose

```bash
docker-compose up --build
```

## License

MIT