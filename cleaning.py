import re #regular expression

def clean_text(text):
    """
    Basic cleaning: lowercase + remove non-alphabetic chars
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text
