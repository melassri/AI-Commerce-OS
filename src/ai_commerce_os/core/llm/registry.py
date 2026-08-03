from ai_commerce_os.core.llm.exceptions import (
    ProviderAlreadyRegisteredError,
    ProviderNotFoundError,
)
from ai_commerce_os.core.llm.provider import LLMProvider


class LLMRegistry:
    """In-memory registry for resolving LLM providers by name."""

    def __init__(self) -> None:
        self._providers: dict[str, LLMProvider] = {}

    def register_provider(self, provider: LLMProvider) -> None:
        """Register a provider with a unique stable name."""
        if provider.provider_name in self._providers:
            raise ProviderAlreadyRegisteredError(
                f"Provider '{provider.provider_name}' is already registered."
            )
        self._providers[provider.provider_name] = provider

    def get_provider(self, provider_name: str) -> LLMProvider:
        """Return the registered provider with the requested name."""
        try:
            return self._providers[provider_name]
        except KeyError as error:
            raise ProviderNotFoundError(f"Provider '{provider_name}' is not registered.") from error

    def list_providers(self) -> list[LLMProvider]:
        """Return registered providers in registration order."""
        return list(self._providers.values())
