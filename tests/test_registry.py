import pytest

import ideaforge
from ideaforge.fakes import FakeClient
from ideaforge.llm import LLMClient
from ideaforge.registry import Registry, embedders, llm_clients


def make_registry() -> Registry[LLMClient]:
    return Registry[LLMClient]("llm_client")


def test_create_returns_registered_type() -> None:
    registry = make_registry()
    registry.register("fake", FakeClient)
    assert isinstance(registry.create("fake"), FakeClient)


def test_create_returns_a_fresh_instance_each_time() -> None:
    registry = make_registry()
    registry.register("fake", FakeClient)
    assert registry.create("fake") is not registry.create("fake")


def test_duplicate_name_raises_value_error() -> None:
    registry = make_registry()
    registry.register("fake", FakeClient)
    with pytest.raises(ValueError):
        registry.register("fake", FakeClient)


def test_unknown_name_raises_key_error_listing_available() -> None:
    registry = make_registry()
    registry.register("fake", FakeClient)
    with pytest.raises(KeyError) as error:
        registry.create("missing")
    assert "fake" in str(error.value)


def test_names_are_sorted() -> None:
    registry = make_registry()
    registry.register("b", FakeClient)
    registry.register("a", FakeClient)
    assert registry.names() == ["a", "b"]


def test_new_plugin_works_without_changing_the_sdk() -> None:
    class ShoutingClient:
        def complete(self, prompt: str) -> str:
            return prompt.upper()

    registry = make_registry()
    registry.register("shout", ShoutingClient)
    assert registry.create("shout").complete("hello") == "HELLO"


def test_builtin_components_are_registered_on_import() -> None:
    assert ideaforge is not None
    assert "fake" in llm_clients.names()
    assert "fake" in embedders.names()
