
from app.prompts.builder import build_helpdesk_prompt
from app.embedding.client import generate_response
from app.models.schemas import HelpRequest, ClassificationResult, RetrievalResult

def generate_answer(
    request: HelpRequest,
    classification: ClassificationResult,
    snippets: list[RetrievalResult]
) -> str:
    prompt = build_helpdesk_prompt(
        user_query=request.text,
        classification=classification.model_dump(),
        snippets=[s.model_dump() for s in snippets]
    )
    return generate_response(prompt)
