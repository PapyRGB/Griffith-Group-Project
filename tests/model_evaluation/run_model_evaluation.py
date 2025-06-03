
import os
import sys
import json
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.retriever import retrieve
from src.hf_model import query_huggingface_chat

print("\n📝 Available files in tests/model_evaluation/:")
for f in os.listdir("tests/model_evaluation/questions"):
    if f.endswith(".json"):
        print(f"  - {f}")

print("\n")
questions_filename = input("📂 Enter the name of the JSON file to use for testing questions: ").strip()
QUESTIONS_PATH = Path(f"tests/model_evaluation/questions/{questions_filename}")
RESULTS_PATH = Path("tests/model_evaluation/results.md")

if not QUESTIONS_PATH.exists():
    print(f"\n🚫 File '{questions_filename}' not found. Please check the filename and try again.")
    exit(1)

print(f"\n✅ Using question file: {questions_filename}")

RESULTS_PATH = Path("tests/model_evaluation/results.md")
QUESTIONS_PATH = Path(f"tests/model_evaluation/questions/{questions_filename}")

def count_question_headers(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content.count("## Question")


def load_questions(path):
    print(f"🔍 Loading questions from: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def query_rag(question):
    print(f"🧠 Querying RAG system for:\n→ {question}")
    try:
        context = "\n".join(retrieve(question, top_k=5))
        prompt = f"Use this context to answer:\n{context}\n\nQuestion: {question}"
        print("📥 Retrieved context. Asking the model...")
        answer = query_huggingface_chat(prompt)
        return context, answer.strip()
    except Exception as e:
        print(f"❌ Error while querying RAG: {e}")
        return "", f"**Error:** {str(e)}"


def auto_evaluate(question, context, answer):
    eval_prompt = f"""
You are an evaluator reviewing a student's answer based on source context.

Question: {question}

Context:
{context}

Answer:
{answer}

Evaluate the answer with one of the following ratings: "Correct", "Partially correct", or "Incorrect".
Then briefly explain why in one line.
"""
    try:
        print("🤖 Performing automatic evaluation...")
        evaluation = query_huggingface_chat(eval_prompt)
        return evaluation.strip()
    except Exception as e:
        return f"**Evaluation Error:** {str(e)}"


def write_result(md_path, question, answer, index, evaluation):
    print(f"📝 Writing result for Question {index + 1} to {md_path.name}")
    with open(md_path, "a", encoding="utf-8") as f:
        f.write("\n\n")
        f.write(f"## Question {index + 1}: {question}\n\n")
        f.write(f"**RAG Answer:**\n{answer}\n\n")
        f.write(f"**Evaluation (automatic):**\n{evaluation}\n\n")
        f.write("**Human Evaluation**  \n")
        f.write("_Keep one of the following:_  \n\n")
        f.write("- [ ] ✅ Correct — Fully answers the question based on context.  \n")
        f.write("- [ ] 🟡 Partially correct — Some accurate info, but incomplete or unclear.  \n")
        f.write("- [ ] ❌ Incorrect — Answer is wrong or unsupported by context.\n\n")
        f.write("---\n\n")


def initialize_results_file(md_path):
    if md_path.exists() and md_path.stat().st_size == 0:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("<!-- markdownlint-disable MD033 -->\n\n")
            f.write("# Model evaluation\n\n")
            f.write("---\n")


def main():
    if not QUESTIONS_PATH.exists():
        print(f"🚫 Question file not found: {QUESTIONS_PATH}")
        return
    
    initialize_results_file(RESULTS_PATH)
    
    INITIAL_QUESTIONS_INDEX = count_question_headers(RESULTS_PATH)
    questions = load_questions(QUESTIONS_PATH)
    print(f"✅ {len(questions)} questions loaded.\n")

    for idx, item in enumerate(questions):
        idx += INITIAL_QUESTIONS_INDEX
        question = item.get("question")
        if not question:
            print(f"⚠️ Skipping invalid entry at index {idx}")
            continue

        context, answer = query_rag(question)
        evaluation = auto_evaluate(question, context, answer)
        write_result(RESULTS_PATH, question, answer, idx, evaluation)
        print(f"✅ Finished Question {idx + 1}\n")

    print("🎉 Evaluation complete.")


if __name__ == "__main__":
    main()
