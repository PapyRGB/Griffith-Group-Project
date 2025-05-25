from src.hf_model import query_huggingface
import os
import pytest

@pytest.mark.skipif(not os.getenv("HF_API_TOKEN"), reason="HF_API_TOKEN not set")
def test_query_huggingface():
    prompt = "What is Griffith College?"
    response = query_huggingface(prompt)
    assert isinstance(response, str)
    assert len(response) > 0