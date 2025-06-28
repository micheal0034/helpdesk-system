# app/retrieval/indexer.py
import os
import glob
import json
import numpy as np
import faiss
from typing import List, Tuple, Dict

from app.embedding.client import embed_text
from app.retrieval.chunking import chunk_text, extract_strings

class Indexer:
    """
    Builds a FAISS vector index from .md and .json documents.
    """
    def __init__(self, data_dir: str, index_path: str):
        self.data_dir = data_dir
        self.index_path = index_path

    def load_documents(self) -> List[Tuple[str, str]]:
        docs = []

        # Markdown files
        for md_file in glob.glob(os.path.join(self.data_dir, "*.md")):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            docs.append((os.path.basename(md_file), content))

        # JSON files
        for json_file in glob.glob(os.path.join(self.data_dir, "*.json")):
            with open(json_file, 'r', encoding='utf-8') as f:
                content = json.load(f)
            strings = extract_strings(content)
            for i, text in enumerate(strings):
                doc_id = f"{os.path.basename(json_file)}#chunk{i}"
                docs.append((doc_id, text))

        return docs

    def build_index(self) -> None:
        docs = self.load_documents()
        embeddings = []
        metadatas = []

        for doc_id, text in docs:
            for chunk in chunk_text(text):
                emb = embed_text(chunk).astype('float32')
                embeddings.append(emb)
                metadatas.append({'id': doc_id, 'text': chunk})

        if not embeddings:
            print(f"No documents found in {self.data_dir}. Nothing to index.")
            return

        dim = embeddings[0].shape[0]
        index = faiss.IndexFlatL2(dim)
        index.add(np.stack(embeddings))

        faiss.write_index(index, self.index_path)
        with open(self.index_path + '.meta', 'w', encoding='utf-8') as f:
            json.dump(metadatas, f)

        print(f"✅ Index built and saved to: {self.index_path}")
    
    
if __name__ == "__main__":
    # Example usage
    indexer = Indexer(data_dir="data", index_path="data/faiss_index")
    indexer.build_index()
    print("Indexing complete.")