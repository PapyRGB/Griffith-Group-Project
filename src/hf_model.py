from huggingface_hub import InferenceClient
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# Create the client
client = InferenceClient(
    model="mistralai/Mistral-Small-3.1-24B-Instruct-2503",
    token=HF_API_TOKEN,
    provider="nebius",  # Remove this line if you're not using Nebius
)

# Query function using chat-style messages
def query_huggingface_chat(prompt: str, system_message: str = None) -> str:
    messages = []

    if system_message:
        messages.append({"role": "system", "content": system_message})

    messages.append({"role": "user", "content": prompt})

    # Make chat completion request
    completion = client.chat.completions.create(
        model="mistralai/Mistral-Small-3.1-24B-Instruct-2503",
        messages=messages
    )

    return completion.choices[0].message.content
