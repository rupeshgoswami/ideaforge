# ideaforge

ideaforge is a small Python SDK for building AI applications from swappable
parts: language models, embedders, retrievers and tools. Components are
registered by name, so you can change providers through configuration and test
everything without an API key.

## Quickstart

Install from a clone:

```
git clone https://github.com/YOUR-USERNAME/ideaforge.git
cd ideaforge
uv sync
uv run pytest
```

Register your own component. No inheritance and no changes to the SDK are needed:

```python
from ideaforge.registry import llm_clients


class MyClient:
    def complete(self, prompt: str) -> str:
        return "hello from my plugin"


llm_clients.register("mine", MyClient)
print(llm_clients.create("mine").complete("hi"))
```

Run the API:

```
uv run uvicorn ideaforge.api:app --reload
```

Then open http://localhost:8000/docs for interactive documentation.

Start the database (Postgres with pgvector):

```
docker compose up -d
```

## Design patterns and where they live

| Pattern | What it does here | File |
| --- | --- | --- |
| Protocol (structural typing) | Defines what a model, embedder, retriever or tool must do, without forcing inheritance | `interfaces.py`, `llm.py` |
| Factory | Builds components from a name | `registry.py` |
| Registry | One central lookup that new components join | `registry.py` |
| Open/closed principle | Extend by registering, never by editing the core | `registry.py` |
| Dependency injection | API routes receive components through FastAPI `Depends` | `api.py` |
| Test double | Fake components for key-free, network-free tests | `fakes.py` |
| Plugin discovery | Installed packages add components through entry points | `registry.py` |

## Project checks

CI runs ruff, mypy (strict) and pytest on every push.

## Roadmap

RAG with pgvector, streaming chat API, agents, evals, documentation site.