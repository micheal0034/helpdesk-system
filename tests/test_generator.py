# tests/test_generator.py
from app.services.generator import generate_answer
from app.models.schemas import HelpRequest, ClassificationResult, RetrievalResult

def test_generate_answer_format():
    req = HelpRequest(text="I can't access VPN")
    classification = ClassificationResult(label="VPN", confidence=0.88, escalate=False)
    snippets = [RetrievalResult(id="doc1", text="To access VPN, go to...", distance=0.12)]

    response = generate_answer(req, classification, snippets)

    assert isinstance(response, str)
    assert len(response) > 0
