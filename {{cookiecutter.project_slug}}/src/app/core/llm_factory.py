from typing import Any

from langchain.chat_models import init_chat_model

from app.core.config import settings


def get_chat_model() -> Any:
    provider = settings.llm_provider.lower()

    if provider == "openai":
        return init_chat_model(
            model=settings.openai_model,
            model_provider="openai",
            temperature=0,
        )

    if provider == "anthropic":
        return init_chat_model(
            model=settings.anthropic_model,
            model_provider="anthropic",
            temperature=0,
        )

    if provider == "azure_openai":
        return init_chat_model(
            model=settings.azure_openai_deployment,
            model_provider="azure_openai",
            api_key=settings.azure_openai_api_key,
            base_url=settings.azure_openai_endpoint,
            temperature=0,
        )

    raise ValueError(f"Unsupported provider: {provider}")
