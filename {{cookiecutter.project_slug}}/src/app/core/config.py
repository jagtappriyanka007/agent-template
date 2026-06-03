from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "dev"
    log_level: str = "INFO"

    llm_provider: str = "{{ cookiecutter.llm_provider }}"
    openai_api_key: str = ""
    openai_model: str = "{{ cookiecutter.openai_model }}"

    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    azure_openai_deployment: str = ""

    anthropic_api_key: str = ""
    anthropic_model: str = "{{ cookiecutter.anthropic_model }}"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
