"""Stand-in components for tests. They need no API key, database or network."""

from ideaforge.models import Document, SearchResult


class FakeClient:
    """A stand-in model. Returns a fixed reply."""

    def __init__(self, reply: str = "fake reply") -> None:
        self.reply = reply

    def complete(self, prompt: str) -> str:
        return self.reply


class FakeEmbedder:
    """Returns a vector of the same length for every text."""

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[float(len(text)), 1.0] for text in texts]


class InMemoryRetriever:
    """Returns the first k stored documents, each with score 1.0."""

    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents

    def search(self, query: str, k: int) -> list[SearchResult]:
        return [SearchResult(document=doc, score=1.0) for doc in self.documents[:k]]
