
import os
import sys
import json
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.retriever import retrieve
from src.hf_model import query_huggingface_chat

RESULTS_PATH = Path("tests/model_evaluation/results.md")
QUESTIONS_PATH = Path("tests/model_evaluation/evaluation_question_1.json")


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
        f.write("_Check one of the following:_  \n\n")
        f.write("- [ ] ✅ Correct — Fully answers the question based on context.  \n")
        f.write("- [ ] 🟡 Partially correct — Some accurate info, but incomplete or unclear.  \n")
        f.write("- [ ] ❌ Incorrect — Answer is wrong or unsupported by context.\n\n")
        f.write("---\n\n")


def main():
    if not QUESTIONS_PATH.exists():
        print(f"🚫 Question file not found: {QUESTIONS_PATH}")
        return

    questions = load_questions(QUESTIONS_PATH)
    print(f"✅ {len(questions)} questions loaded.\n")

    for idx, item in enumerate(questions):
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
