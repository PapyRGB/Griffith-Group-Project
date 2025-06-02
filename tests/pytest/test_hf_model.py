import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.hf_model import query_huggingface_chat
import pytest
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

@pytest.mark.skipif(not os.getenv("HF_API_TOKEN"), reason="HF_API_TOKEN not set")
def test_query_huggingface_chat():
    prompt = "What is Griffith College?"
    response = query_huggingface_chat(prompt)
    assert isinstance(response, str)
    assert len(response.strip()) > 0
