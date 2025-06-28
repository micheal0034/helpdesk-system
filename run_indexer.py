# run_indexer.py
from app.retrieval.indexer import Indexer

if __name__ == "__main__":
    indexer = Indexer(data_dir="data", index_path="data/faiss.index")
    indexer.build_index()
