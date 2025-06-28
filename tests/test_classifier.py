# tests/test_classifier.py
from app.services.classifier import classify_request

def test_classifier_basic():
    text = "My email is not working"
    result = classify_request(text)
    
    assert result.label is not None
    assert 0 <= result.confidence <= 1
    assert isinstance(result.escalate, bool)
