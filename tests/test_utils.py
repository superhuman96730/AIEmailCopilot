from app.utils import extract_email_metadata, sanitize_email_body

def test_extract_email_metadata():
    text = "Line 1\\nLine 2\\nLine 3"
    result = extract_email_metadata(text)
    assert "line_count" in result
    assert "char_count" in result

def test_sanitize_email_body():
    text = "  HELLO WORLD  "
    result = sanitize_email_body(text)
    assert result == "hello world"
