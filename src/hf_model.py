import requests
import os

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query_huggingface(prompt: str, max_tokens: int = 300):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "temperature": 0.7
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()[0]["generated_text"]