import inspect
from collections.abc import Sequence

from ai_commerce_os.core.llm.models import LLMMessage, LLMResponse
from ai_commerce_os.core.llm.provider import LLMProvider


class ExampleProvider(LLMProvider):
    @property
    def provider_name(self) -> str:
        return "example"

    def chat(self, messages: Sequence[LLMMessage]) -> LLMResponse:
        return LLMResponse(
            content=messages[0].content,
            model="example-model",
            provider=self.provider_name,
            input_tokens=1,
            output_tokens=1,
        )

    def models(self) -> Sequence[str]:
        return ["example-model"]


def test_llm_provider_is_abstract() -> None:
    assert inspect.isabstract(LLMProvider)


def test_llm_provider_contract() -> None:
    provider = ExampleProvider()
    response = provider.chat([LLMMessage(role="user", content="Hello")])

    assert provider.provider_name == "example"
    assert provider.models() == ["example-model"]
    assert response.content == "Hello"
