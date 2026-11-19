"""Example plugins, also used to test entry-point discovery."""


class ShoutingClient:
    """Returns the prompt in upper case."""

    def complete(self, prompt: str) -> str:
        return prompt.upper()