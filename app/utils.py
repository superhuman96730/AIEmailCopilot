def extract_email_metadata(email_text: str) -> dict:
    """Extract metadata from email text."""
    lines = email_text.split("\n")
    return {
        "line_count": len(lines),
        "char_count": len(email_text),
        "has_attachments": "attachment" in email_text.lower()
    }

def sanitize_email_body(body: str) -> str:
    """Clean and normalize email body text."""
    return body.strip().lower()
