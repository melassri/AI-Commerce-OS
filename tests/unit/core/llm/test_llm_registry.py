from collections.abc import Sequence

import pytest

from ai_commerce_os.core.llm.exceptions import (
    LLMError,
    ProviderAlreadyRegisteredError,
    ProviderNotFoundError,
)
from ai_commerce_os.core.llm.models import LLMMessage, LLMResponse
from ai_commerce_os.core.llm.provider import LLMProvider
from ai_commerce_os.core.llm.registry import LLMRegistry


class StubProvider(LLMProvider):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def provider_name(self) -> str:
        return self._name

    def chat(self, messages: Sequence[LLMMessage]) -> LLMResponse:
        return LLMResponse(
            content="",
            model="stub-model",
            provider=self.provider_name,
            input_tokens=0,
            output_tokens=0,
        )

    def models(self) -> Sequence[str]:
        return []


def test_registry_registers_and_resolves_provider() -> None:
    registry = LLMRegistry()
    provider = StubProvider("stub")

    registry.register_provider(provider)

    assert registry.get_provider("stub") is provider
    assert registry.list_providers() == [provider]


def test_registry_raises_for_unknown_provider() -> None:
    with pytest.raises(ProviderNotFoundError, match="not registered"):
        LLMRegistry().get_provider("unknown")


def test_registry_rejects_duplicate_provider_names() -> None:
    registry = LLMRegistry()
    registry.register_provider(StubProvider("stub"))

    with pytest.raises(ProviderAlreadyRegisteredError, match="already registered"):
        registry.register_provider(StubProvider("stub"))


@pytest.mark.parametrize(
    "exception_type",
    [ProviderNotFoundError, ProviderAlreadyRegisteredError],
)
def test_provider_errors_inherit_from_llm_error(
    exception_type: type[LLMError],
) -> None:
    assert isinstance(exception_type(), LLMError)
