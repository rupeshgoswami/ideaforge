from ideaforge.llm import FakeClient, LLMClient


def test_fake_client_returns_reply() -> None:
    client: LLMClient = FakeClient(reply="hello")
    assert client.complete("anything") == "hello"
