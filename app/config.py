from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    google_application_credentials: str

    model_config = SettingsConfigDict(env_file=".local_env")

def get_settings() -> Settings:
    settings = Settings()
    return settings