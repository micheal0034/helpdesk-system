from app.embedding.client import embed_text
from app.models.schemas import ClassificationResult
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.core.config import settings


class RequestClassifier:
    def __init__(self, path=None, threshold: float = 0.6, trigger_threshold: float = 0.4):
        path = path or settings.CATEGORIES_PATH

        with open(path, 'r') as f:
            self.categories = json.load(f).get('categories', {})

        self.threshold = threshold
        self.trigger_threshold = trigger_threshold

        # Precompute all embeddings
        self.category_embeddings = {}
        self.trigger_embeddings = {}

        for cat, props in self.categories.items():
            description = props.get("description", "")
            self.category_embeddings[cat] = embed_text(description)

            triggers = props.get("escalation_triggers", [])
            self.trigger_embeddings[cat] = [embed_text(t) for t in triggers]

    def predict(self, text: str):
        text_emb = embed_text(text)

        # Step 1: Classify via semantic similarity to category description
        similarities = {
            cat: cosine_similarity([text_emb], [emb])[0][0]
            for cat, emb in self.category_embeddings.items()
        }
        label = max(similarities, key=similarities.get)
        confidence = similarities[label]

        # Step 2: Check escalation
        escalate = self._should_escalate(label, text_emb, confidence)

        return label, confidence, escalate

    def _should_escalate(self, label: str, text_emb: np.ndarray, confidence: float) -> bool:        
        # Rule 2: High semantic similarity to any escalation trigger
        trigger_embs = self.trigger_embeddings.get(label, [])
        for trig_emb in trigger_embs:
            trig_sim = cosine_similarity([text_emb], [trig_emb])[0][0]
            if trig_sim >= self.trigger_threshold:
                return True
            
        # # Rule 1: Low classification confidence
        # if confidence < self.threshold:
        #     return True

        return False


# Singleton instance
_classifier = RequestClassifier()

def classify_request(text: str) -> ClassificationResult:
    label, confidence, escalate = _classifier.predict(text)
    return ClassificationResult(label=label, confidence=confidence, escalate=escalate)

