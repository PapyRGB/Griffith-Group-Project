from docx import Document
import fitz  # PyMuPDF

def load_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

def load_pdf(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks