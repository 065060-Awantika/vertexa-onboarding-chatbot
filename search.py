import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("kb_index.faiss")

with open("kb_chunks.pkl", "rb") as f:
    data = pickle.load(f)
    chunks = data["chunks"]
    sources = data["sources"]

def search(query, top_k=3):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    results = []
    for idx in indices[0]:
        results.append({"text": chunks[idx], "source": sources[idx]})
    return results

if __name__ == "__main__":
    query = input("Ask a question: ")
    results = search(query)
    for r in results:
        print(f"\n--- From {r['source']} ---")
        print(r["text"][:300], "...")