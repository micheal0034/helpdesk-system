
import json
import numpy as np
import faiss
from app.embedding.client import embed_text
from app.models.schemas import RetrievalResult
from app.core.config import settings

class Retriever:
    def __init__(self, index_path=None):
        index_path = index_path or settings.INDEX_PATH
        self.index = faiss.read_index(index_path)
        with open(index_path + '.meta', 'r', encoding='utf-8') as f:
            self.metadatas = json.load(f)

    def search(self, query: str, k: int = 5):
        emb = embed_text(query).astype('float32')
        distances, indices = self.index.search(np.array([emb]), k)
        return [
            RetrievalResult(id=self.metadatas[idx]['id'], text=self.metadatas[idx]['text'], distance=float(dist))
            for dist, idx in zip(distances[0], indices[0])
        ]

# Singleton instance
_retriever = Retriever()

def retrieve_knowledge(text: str, k: int = 5):
    return _retriever.search(text, k)
