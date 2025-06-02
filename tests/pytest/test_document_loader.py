import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.document_loader import load_docx, load_pdf, chunk_text

def test_chunk_text():
    text = "This is a sample text for testing chunking." * 20
    chunks = chunk_text(text, chunk_size=100, overlap=20)
    assert len(chunks) > 1
    assert all(isinstance(chunk, str) for chunk in chunks)

def test_load_docx():
    path = "data/original_data/Admin Info.docx"
    if os.path.exists(path):
        text = load_docx(path)
        assert isinstance(text, str)
        assert len(text) > 0

def test_load_pdf():
    path = "data/original_data/griffith-college-student-handbook-2024-25.pdf"
    if os.path.exists(path):
        text = load_pdf(path)
        assert isinstance(text, str)
        assert len(text) > 0