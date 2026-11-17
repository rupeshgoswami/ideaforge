from ideaforge.fakes import FakeClient
from ideaforge.llm import LLMClient


def test_fake_client_returns_reply() -> None:
    client: LLMClient = FakeClient(reply="hello")
    assert client.complete("anything") == "hello"
