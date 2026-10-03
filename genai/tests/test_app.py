import os

from app import ask_question


class FakeDoc:
    def __init__(self, page_content):
        self.page_content = page_content


class FakeLLM:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def invoke(self, prompt):
        class Response:
            content = "This is a test answer based on the provided context."

        return Response()


def test_ask_question_returns_answer(monkeypatch):
    monkeypatch.setenv("OPENAI_MODEL", "gpt-4o-mini")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("TOP_K", "2")

    monkeypatch.setattr(
        "app.similarity_search",
        lambda question, k=4: [FakeDoc("Context A"), FakeDoc("Context B")],
    )
    monkeypatch.setattr("app.ChatOpenAI", lambda **kwargs: FakeLLM(**kwargs))

    result = ask_question("What is the answer?")

    assert "test answer" in result.lower()
    assert "provided context" in result.lower()


def test_ask_question_uses_top_k_from_env(monkeypatch):
    monkeypatch.setenv("TOP_K", "3")

    called = {}

    def fake_similarity_search(query, k=4):
        called["k"] = k
        return [FakeDoc("Only context")]

    monkeypatch.setattr("app.similarity_search", fake_similarity_search)
    monkeypatch.setattr("app.ChatOpenAI", lambda **kwargs: FakeLLM(**kwargs))

    ask_question("Test query")

    assert called["k"] == 3
