from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI TODO Test App")
    database_url: str = Field(default="sqlite:///./db.sqlite3")
    cors_origins: list[str] = Field(default_factory=lambda: ["*"])

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
