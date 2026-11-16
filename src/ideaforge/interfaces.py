from typing import Protocol

from ideaforge.models import SearchResult


class Embedder(Protocol):
    """Turns a list of texts into vector embeddings."""

    def embed(self, texts: list[str]) -> list[list[float]]: ...


class Retriever(Protocol):
    """Searches for documents relevant to a query string."""

    def search(self, query: str, k: int) -> list[SearchResult]: ...


class Tool(Protocol):
    """A callable tool that an agent can invoke."""

    @property
    def name(self) -> str: ...

    @property
    def description(self) -> str: ...

    def run(self, arguments: dict[str, str]) -> str: ...
