# Griffith-Group-Project

Griffith 3rd year, second semester, Group Project - [BSCO-GP/Dub/FT]

## 🌿 Initial Branch Structure

| Branch Name                   | Purpose                                                             |
|-------------------------------|---------------------------------------------------------------------|
| `main`                        | Stable, production-ready code                                       |
| `dev`                         | Active development integration branch                               |
| `feature/docs_static_loader` | One-time ingestion of `.docx` and `.pdf` documents                  |
| `feature/embedding_faiss`     | Embedding generation and FAISS index creation                       |
| `feature/model_hf_api`        | Hugging Face Inference API integration                              |
| `feature/model_llama_local`   | Optional local LLM (`llama.cpp`) support                            |
| `feature/rag_retrieval`       | Retrieval logic to fetch relevant chunks based on queries           |
| `feature/streamlit_frontend`  | Streamlit interface, caching decorators, and session management     |
| `feature/query_eval_testing`  | Evaluation with sample queries, validation output, test harness     |
| `feature/deploy_config`       | Streamlit Cloud setup, environment vars, secrets, and deployment docs |

## 🧱 Finalized Stack Plan

This project implements a Retrieval-Augmented Generation (RAG) assistant for Griffith College student documents, using modern open-source LLM and embedding tools.

| Component       | Choice                                      | Notes |
|----------------|---------------------------------------------|-------|
| **LLM**         | Hugging Face Inference API (`mistralai/Mistral-7B-Instruct-v0.1`) | Default for Streamlit Cloud |
|                | `llama.cpp` (local)                         | Optional for local/private use |
| **Embeddings**  | `BAAI/bge-small-en`                        | Accurate and efficient |
|                | `all-MiniLM-L6-v2`                          | Lightweight fallback |
| **Vector Store**| FAISS (in-memory)                          | Perfect for fixed static documents |
|                | Pinecone (optional)                         | Can be toggled for scalability |
| **Frontend**    | Streamlit Cloud App                        | User interface with query input/output |
| **Caching**     | `@st.cache_data`                           | Used for embeddings and static data |
| **Document Sources** | `Admin Info.docx` and `griffith-college-student-handbook-2024-25.pdf` | No new uploads expected from users |

> Streamlit Cloud does not support running `llama.cpp` directly, so use Hugging Face Inference API for deployment. Local `llama.cpp` is supported for demos or offline use.
