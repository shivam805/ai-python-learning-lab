from vector_store import similarity_search


class FakeStore:
    def similarity_search(self, query, k=4):
        assert query == "sample question"
        assert k == 5
        return ["doc1", "doc2"]


class FakeEmbeddings:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


def test_similarity_search_forwards_k(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr("vector_store.OpenAIEmbeddings", FakeEmbeddings)
    monkeypatch.setattr("vector_store.Chroma", lambda **kwargs: FakeStore())

    result = similarity_search("sample question", k=5)

    assert result == ["doc1", "doc2"]
