from abc import ABC, abstractmethod
from collections.abc import Sequence

from ai_commerce_os.core.llm.models import LLMMessage, LLMResponse


class LLMProvider(ABC):
    """Port implemented by future LLM provider adapters."""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider's stable identifier."""
        ...

    @abstractmethod
    def chat(self, messages: Sequence[LLMMessage]) -> LLMResponse:
        """Return a response for a sequence of messages."""
        ...

    @abstractmethod
    def models(self) -> Sequence[str]:
        """Return the models exposed by this provider."""
        ...
