# 🎓 Griffith-Group-Project

> 3rd Year BSc (Hons) in Computing — Group Project  
> **Griffith College, Dublin** · BSCO-GP/Dub/FT · 2024–2025  
> Supervisor: Dr. Waseem Akhtar

This project implements a **Retrieval-Augmented Generation (RAG) assistant** tailored to Griffith College student documents. The assistant can ingest `.docx` and `.pdf` files (such as the official Student Handbook and Admin Info guide) and intelligently respond to user queries using LLMs, embeddings, and a custom-built retrieval pipeline.

---

## 🏗️ Project Overview

- **Goal:** Assist Griffith College students by enabling natural language queries over static academic documents.
- **Input Sources:**  
  - `Admin Info.docx` – internal faculty guidance  
  - `griffith-college-student-handbook-2024-25.pdf` – official student guide
- **Approach:**  
  A streamlined RAG architecture using pre-trained models, embeddings, FAISS for retrieval, and Streamlit for interface.

---

## 🌿 Branch Structure

| Branch                        | Purpose                                                             |
|------------------------------|---------------------------------------------------------------------|
| `main`                       | Stable, production-ready code                                       |
| `dev`                        | Active development integration                                      |
| `feature/docs_static_loader`| One-time ingestion of `.docx` and `.pdf` documents                  |
| `feature/embedding_faiss`    | Embedding generation and FAISS index creation                       |
| `feature/model_hf_api`       | Hugging Face Inference API integration                              |
| `feature/model_llama_local`  | Optional local LLM (`llama.cpp`) support                            |
| `feature/rag_retrieval`      | Retrieval logic to fetch relevant chunks based on queries           |
| `feature/streamlit_frontend` | Streamlit interface, caching decorators, and session management     |
| `feature/query_eval_testing` | Evaluation with sample queries, validation output, test harness     |
| `feature/deploy_config`      | Streamlit Cloud setup, environment vars, secrets, and deployment docs |

---

## 🧱 Stack Summary

| Layer             | Technology / Tool                                   | Purpose/Notes                                          |
|------------------|-----------------------------------------------------|--------------------------------------------------------|
| **Frontend**      | Streamlit                                           | UI for student queries                                 |
| **LLM**           | Hugging Face Inference API (Mistral-7B)            | Hosted model for production use                        |
|                  | `llama.cpp` (optional local use)                    | For demos or offline queries                           |
| **Embeddings**    | `BAAI/bge-small-en` (default)                      | Robust semantic embedding generation                   |
|                  | `all-MiniLM-L6-v2` (fallback)                       | Lightweight alternative                                |
| **Vector Store**  | FAISS                                               | Fast similarity search over document chunks            |
| **Caching**       | `@st.cache_data` (Streamlit)                       | Performance boost for repeat queries and startup       |
| **Storage**       | In-memory only                                     | No persistent user uploads supported                   |
| **Documents**     | `Admin Info.docx`, `griffith-college-student-handbook-2024-25.pdf` | Ingested once, read-only context                       |

---

## 🚀 Deployment

- **Production:** Streamlit Cloud with Hugging Face API (`mistralai/Mistral-7B-Instruct-v0.1`)
- **Local:** Optional `llama.cpp` with GGUF model support for offline use
- ⚠️ Note: Streamlit Cloud does **not** support local binaries like `llama.cpp`

---

## ✅ Features

- 🧠 Question answering from Griffith documents
- 📄 Chunked ingestion and vectorized semantic search
- 🔎 Fast FAISS-based document retrieval
- 🧪 Sample query testing and evaluation scripts
- 📦 Streamlit UI with dynamic session and caching
- 🛠️ Ready for Streamlit Cloud deployment

---

## 📁 Project Structure

```bash
Griffith-Group-Project/
├── streamlit_app/             # Streamlit UI
├── src/                          # RAG pipeline logic
│   ├── document_loader.py        # PDF and DOCX ingestion
│   ├── embed_index.py            # SentenceTransformer wrapper
│   ├── hf_model.py               # HuggingFace and llama.cpp clients
│   └── retriever.py              # FAISS integration
├── tests/                        # Pytest units testing 
│   ├── model_evaluation/         # Model evaluation script
│   └── pytest/                   # Pytest unit testing   
├── data/                         # Static documents and vector stores
└── README.md
```

---

## 👥 Team Group 1

- [Maxime Viel](https://github.com/PapyRGB)
- [Benoît Catez](https://github.com/LimuleSempai)

---

## 📌 References

- [Griffith College Student Handbook 2024–25](https://www.griffith.ie/)
- [Admin Info (Computing Faculty)](https://www.griffith.ie/faculties/computing-science)
- [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- [BAAI/bge-small-en](https://huggingface.co/BAAI/bge-small-en)
- [SentenceTransformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
