class LLMError(Exception):
    """Base error raised by LLM core operations."""


class ProviderNotFoundError(LLMError):
    """Raised when a provider name is not registered."""


class ProviderAlreadyRegisteredError(LLMError):
    """Raised when a provider name is already registered."""
