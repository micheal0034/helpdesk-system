from pydantic import BaseModel
from typing import List

class HelpRequest(BaseModel):
    text: str

class ClassificationResult(BaseModel):
    label: str
    confidence: float
    escalate: bool

class RetrievalResult(BaseModel):
    id: str
    text: str
    distance: float

class HelpResponse(BaseModel):
    classification: ClassificationResult
    snippets: List[RetrievalResult]
    answer: str