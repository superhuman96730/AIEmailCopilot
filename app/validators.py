import re

def validate_email_address(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_email_body(body: str) -> bool:
    return body is not None and len(body.strip()) > 0
