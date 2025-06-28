
from typing import Any, List

def chunk_text(text: str, max_tokens: int = 200) -> List[str]:
    """
    Splits long text into smaller chunks of approximately `max_tokens` length.
    """
    tokens = text.split()
    return [" ".join(tokens[i:i+max_tokens]) for i in range(0, len(tokens), max_tokens)]

def extract_strings(obj: Any) -> List[str]:
    """
    Recursively extract all string values from nested JSON-like structures.
    """
    texts = []
    if isinstance(obj, dict):
        for v in obj.values():
            texts.extend(extract_strings(v))
    elif isinstance(obj, list):
        for v in obj:
            texts.extend(extract_strings(v))
    elif isinstance(obj, str):
        texts.append(obj)
    return texts
