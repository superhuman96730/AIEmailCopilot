def count_words(text: str) -> int:
    return len(text.split())

def count_sentences(text: str) -> int:
    return len(text.split('.'))

def get_text_complexity(text: str) -> str:
    words = count_words(text)
    if words < 50:
        return "low"
    elif words < 200:
        return "medium"
    else:
        return "high"
