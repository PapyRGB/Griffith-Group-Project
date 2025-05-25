from sentence_transformers import SentenceTransformer
import numpy as np
from src.embed_index import load_index, load_chunks

model = SentenceTransformer("BAAI/bge-small-en")
index = load_index()
chunks = load_chunks()

def retrieve(query, top_k=5):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [chunks[i] for i in I[0]]