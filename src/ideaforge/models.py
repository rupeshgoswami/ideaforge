from dataclasses import dataclass, field


@dataclass(frozen=True)
class Document:
    """Represents a piece of text with metadata."""

    id: str
    text: str
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class SearchResult:
    """Represents a retrieved document and its relevance score."""

    document: Document
    score: float
