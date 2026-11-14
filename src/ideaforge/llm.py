from typing import Protocol


class LLMClient(Protocol):
    """Anything that can turn a prompt into a text reply."""

    def complete(self, prompt: str) -> str: ...


class FakeClient:
    """A stand-in model for tests. Returns a fixed reply, needs no API key."""

    def __init__(self, reply: str = "fake reply") -> None:
        self.reply = reply

    def complete(self, prompt: str) -> str:
        return self.reply
