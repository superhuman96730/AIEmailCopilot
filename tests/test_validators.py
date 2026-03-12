from app.validators import validate_email_address, validate_email_body

def test_validate_email_address():
    assert validate_email_address("test@example.com") == True
    assert validate_email_address("invalid-email") == False

def test_validate_email_body():
    assert validate_email_body("Hello world") == True
    assert validate_email_body("") == False
