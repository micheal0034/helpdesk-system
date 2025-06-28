# scripts/build_index.py
import os
from app.retrieval.indexer import Indexer

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(project_root, "data")
    index_path = os.path.join(data_dir, "faiss.index")

    indexer = Indexer(data_dir=data_dir, index_path=index_path)
    indexer.build_index()
