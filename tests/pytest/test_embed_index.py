import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import numpy as np
from src.embed_index import embed_texts, create_faiss_index

def test_embed_texts():
    chunks = ["This is a test chunk.", "Another chunk of text."]
    embeddings = embed_texts(chunks)
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == len(chunks)

def test_create_faiss_index():
    chunks = ["This is a test chunk.", "Another chunk of text."]
    embeddings = embed_texts(chunks)
    index = create_faiss_index(embeddings)
    assert index.ntotal == len(chunks)