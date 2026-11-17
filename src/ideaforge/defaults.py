"""Registers the built-in components. Imported once when the package loads."""

from ideaforge.fakes import FakeClient, FakeEmbedder
from ideaforge.registry import embedders, llm_clients

llm_clients.register("fake", FakeClient)
embedders.register("fake", FakeEmbedder)
