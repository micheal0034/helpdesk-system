
def test_classify_endpoint(client):
    resp = client.post("/api/v1/classify", json={"text": "Outlook is crashing"})
    assert resp.status_code == 200
    data = resp.json()
    assert "label" in data
    assert isinstance(data["escalate"], bool)

def test_helpdesk_endpoint(client):
    resp = client.post("/api/v1/helpdesk", json={"text": "My Teams app won't connect"})
    assert resp.status_code == 200
    data = resp.json()
    assert "answer" in data
    assert "classification" in data
    assert "snippets" in data
