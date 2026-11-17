from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from ideaforge.interfaces import Embedder
from ideaforge.llm import LLMClient
from ideaforge.registry import embedders, llm_clients
from ideaforge.settings import Settings, get_settings

app = FastAPI(title="ideaforge", version="0.1.0")

SettingsDep = Annotated[Settings, Depends(get_settings)]


def get_llm(settings: SettingsDep) -> LLMClient:
    return llm_clients.create(settings.llm_client)


def get_embedder(settings: SettingsDep) -> Embedder:
    return embedders.create(settings.embedder)


LLMDep = Annotated[LLMClient, Depends(get_llm)]
EmbedderDep = Annotated[Embedder, Depends(get_embedder)]


class CompleteRequest(BaseModel):
    prompt: str


class CompleteResponse(BaseModel):
    reply: str


class EmbedRequest(BaseModel):
    texts: list[str]


class EmbedResponse(BaseModel):
    vectors: list[list[float]]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/complete")
def complete(body: CompleteRequest, llm: LLMDep) -> CompleteResponse:
    return CompleteResponse(reply=llm.complete(body.prompt))


@app.post("/v1/embed")
def embed(body: EmbedRequest, embedder: EmbedderDep) -> EmbedResponse:
    return EmbedResponse(vectors=embedder.embed(body.texts))
