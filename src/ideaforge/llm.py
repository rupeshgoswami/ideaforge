from typing import Protocol


class LLMClient(Protocol):
    """Anything that can turn a prompt into a text reply."""

    def complete(self, prompt: str) -> str: ...
