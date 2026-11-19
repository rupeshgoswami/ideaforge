"""A generic plugin registry: look up components by name, add new ones freely."""

from collections.abc import Callable

from ideaforge.interfaces import Embedder, Retriever, Tool
from ideaforge.llm import LLMClient
from importlib.metadata import entry_points


class Registry[T]:
    """Holds factories for one kind of component, keyed by name."""

    def __init__(self, kind: str) -> None:
        self.kind = kind
        self._factories: dict[str, Callable[[], T]] = {}

    def register(self, name: str, factory: Callable[[], T]) -> None:
        """Add a factory. Raises ValueError if the name is already taken."""
        if name in self._factories:
            raise ValueError(f"{self.kind} '{name}' is already registered")
        self._factories[name] = factory

    def create(self, name: str) -> T:
        """Build a fresh component. Raises KeyError for an unknown name."""
        try:
            factory = self._factories[name]
        except KeyError:
            raise KeyError(f"Unknown {self.kind} '{name}'. Available: {self.names()}") from None
        return factory()

    def names(self) -> list[str]:
        """Return registered names, sorted."""
        return sorted(self._factories)
    def load_plugins() -> None:
        """Register components that installed packages declare as entry points."""
        groups = {
            "ideaforge.llm_clients": llm_clients,
            "ideaforge.embedders": embedders,
            "ideaforge.retrievers": retrievers,
            "ideaforge.tools": tools,
        }
        for group, registry in groups.items():
            for entry in entry_points(group=group):
                if entry.name not in registry.names():
                    registry.register(entry.name, entry.load())


llm_clients = Registry[LLMClient]("llm_client")
embedders = Registry[Embedder]("embedder")
retrievers = Registry[Retriever]("retriever")
tools = Registry[Tool]("tool")
