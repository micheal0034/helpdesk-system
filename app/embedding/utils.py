# app/embedding/utils.py
import numpy as np
from typing import List

def normalize(vec: np.ndarray) -> np.ndarray:
    """Normalize a vector to unit length."""
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    v1 = normalize(v1)
    v2 = normalize(v2)
    return float(np.dot(v1, v2))

def batch_embed(texts: List[str], embed_fn) -> List[np.ndarray]:
    """
    Embeds a list of texts using the provided `embed_fn`.
    Useful for batching or reusing.
    """
    return [embed_fn(t) for t in texts]
