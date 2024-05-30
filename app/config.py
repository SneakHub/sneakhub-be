from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_application_credentials: str

    model_config = SettingsConfigDict(env_file=".local_env")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
