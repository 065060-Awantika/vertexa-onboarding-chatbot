import os
import re
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

KB_FOLDER = "knowledge_base"
CHUNK_SIZE = 400
CHUNK_OVERLAP = 50

def load_documents(folder):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            docs.append((filename, text))
    return docs

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def build_index():
    print("Loading documents...")
    docs = load_documents(KB_FOLDER)
    print(f"Loaded {len(docs)} documents.")

    all_chunks = []
    chunk_sources = []

    for filename, text in docs:
        chunks = chunk_text(text)
        for c in chunks:
            all_chunks.append(c)
            chunk_sources.append(filename)

    print(f"Created {len(all_chunks)} chunks.")

    print("Loading embedding model (first run downloads it, ~80MB)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Creating embeddings...")
    embeddings = model.encode(all_chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    print("Building FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, "kb_index.faiss")
    with open("kb_chunks.pkl", "wb") as f:
        pickle.dump({"chunks": all_chunks, "sources": chunk_sources}, f)

    print("Done! Saved kb_index.faiss and kb_chunks.pkl")

if __name__ == "__main__":
    build_index()
