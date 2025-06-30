
from app.services.retriever import retrieve_knowledge

def test_retriever_returns_k_results():
    query = "How do I reset my password?"
    results = retrieve_knowledge(query, k=3)

    assert len(results) <= 3
    for r in results:
        assert "id" in r.model_dump()
        assert "text" in r.model_dump()
