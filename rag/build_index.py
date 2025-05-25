import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.document_loader import load_docx, load_pdf, chunk_text
from src.embed_index import embed_texts, create_faiss_index, save_index, save_chunks

# Load your documents
text1 = load_docx("data/Admin Info.docx")
text2 = load_pdf("data/griffith-college-student-handbook-2024-25.pdf")

# Chunk them
all_chunks = chunk_text(text1) + chunk_text(text2)

# Embed and build index
embeddings = embed_texts(all_chunks)
index = create_faiss_index(embeddings)

# Save results
save_index(index)
save_chunks(all_chunks)
print("FAISS index and chunks saved.")