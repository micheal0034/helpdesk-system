# app/services/helpdesk.py
from app.models.schemas import HelpRequest, HelpResponse
from app.services.classifier import classify_request
from app.services.retriever import retrieve_knowledge
from app.services.generator import generate_answer

def process_helpdesk_request(text: str, k: int = 5) -> HelpResponse:
    # Step 1: Classification
    classification = classify_request(text)

    # Step 2: Knowledge Retrieval
    snippets = retrieve_knowledge(text, k)

    # Step 3: Answer Generation
    from app.models.schemas import HelpRequest as HR  # avoid circular import
    answer = generate_answer(HR(text=text), classification, snippets)

    return HelpResponse(
        classification=classification,
        snippets=snippets,
        answer=answer
    )
