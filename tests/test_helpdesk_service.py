
from app.services.helpdesk import process_helpdesk_request

def test_helpdesk_pipeline():
    text = "My Microsoft Teams won't launch"
    response = process_helpdesk_request(text)

    assert response.classification.label
    assert isinstance(response.answer, str)
    assert isinstance(response.snippets, list)
