from ideaforge.models import Document, SearchResult


class FakeClient:
    """A stand-in LLM model for tests. Returns a fixed reply without network calls."""

    def __init__(self, reply: str = "fake reply") -> None:
        self.reply = reply

    def complete(self, prompt: str) -> str:
        return self.reply


class FakeEmbedder:
    """Returns a mock embedding vector based on text length."""

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[float(len(text)), 1.0] for text in texts]


class InMemoryRetriever:
    """A simple in-memory retriever for testing purposes."""

    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents

    def search(self, query: str, k: int) -> list[SearchResult]:
        # Return the first k documents with a mock score of 1.0
        selected = self.documents[:k]
        return [SearchResult(document=doc, score=1.0) for doc in selected]
