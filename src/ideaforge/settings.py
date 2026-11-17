from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration read from environment variables or a .env file."""

    model_config = SettingsConfigDict(env_file=".env")

    database_url: str = "postgresql://ideaforge:ideaforge_dev@localhost:5432/ideaforge"
    llm_client: str = "fake"
    embedder: str = "fake"


def get_settings() -> Settings:
    return Settings()
