from fastapi.testclient import TestClient

from ideaforge.api import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_complete_uses_fake_client() -> None:
    response = client.post("/v1/complete", json={"prompt": "hi"})
    assert response.status_code == 200
    assert response.json() == {"reply": "fake reply"}


def test_embed_returns_one_vector_per_text() -> None:
    response = client.post("/v1/embed", json={"texts": ["a", "bcd"]})
    assert response.status_code == 200
    assert response.json() == {"vectors": [[1.0, 1.0], [3.0, 1.0]]}


def test_bad_request_is_rejected() -> None:
    response = client.post("/v1/complete", json={"prompt": 123})
    assert response.status_code == 422
