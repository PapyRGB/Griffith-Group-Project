import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import torch
#torch.classes.__path__ = [] # add this line to manually set it to empty.
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 

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