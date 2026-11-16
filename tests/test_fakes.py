from ideaforge.fakes import FakeEmbedder, InMemoryRetriever
from ideaforge.interfaces import Embedder, Retriever
from ideaforge.models import Document


def test_fake_embedder() -> None:
    embedder: Embedder = FakeEmbedder()
    vectors = embedder.embed(["hello", "world"])
    assert len(vectors) == 2
    assert vectors[0] == [5.0, 1.0]


def test_in_memory_retriever() -> None:
    docs = [
        Document(id="1", text="doc one"),
        Document(id="2", text="doc two"),
        Document(id="3", text="doc three"),
    ]
    retriever: Retriever = InMemoryRetriever(documents=docs)
    results = retriever.search("query", k=2)

    assert len(results) == 2
    assert results[0].document.id == "1"
    assert results[1].document.id == "2"
    assert results[0].score == 1.0
