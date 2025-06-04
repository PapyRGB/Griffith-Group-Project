from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

embedding_model = SentenceTransformer('BAAI/bge-small-en')

def embed_texts(text_chunks):
    return embedding_model.encode(text_chunks, show_progress_bar=True)

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_index(index, path="data/faiss_index.idx"):
    faiss.write_index(index, path)

def save_chunks(chunks, path="data/chunks.pkl"):
    with open(path, "wb") as f:
        pickle.dump(chunks, f)

def load_index(path="data/faiss_index.idx"):
    return faiss.read_index(path)

def load_chunks(path="data/chunks.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)