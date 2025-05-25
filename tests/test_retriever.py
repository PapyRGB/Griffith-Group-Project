from src.retriever import retrieve

def test_retrieve():
    query = "What are the rules at Griffith College?"
    results = retrieve(query, top_k=3)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(r, str) for r in results)