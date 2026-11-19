# Changelog

## 0.1.0

- Core interfaces: LLMClient, Embedder, Retriever, Tool
- Generic plugin registry with entry-point discovery
- Fake components for key-free testing
- FastAPI skeleton with /health, /v1/complete, /v1/embed
- CI: ruff, mypy, pytest; Docker Compose with Postgres and pgvector