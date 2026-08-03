from dataclasses import FrozenInstanceError

import pytest

from ai_commerce_os.core.llm.models import LLMMessage, LLMResponse


def test_llm_message_is_immutable() -> None:
    message = LLMMessage(role="user", content="Hello")

    assert message.role == "user"
    assert message.content == "Hello"
    with pytest.raises(FrozenInstanceError):
        message.content = "Updated"  # type: ignore[misc]


def test_llm_response_is_immutable() -> None:
    response = LLMResponse(
        content="Hello",
        model="example-model",
        provider="example-provider",
        input_tokens=4,
        output_tokens=2,
        metadata={"finish_reason": "stop"},
    )

    assert response.model == "example-model"
    assert response.metadata == {"finish_reason": "stop"}
    with pytest.raises(FrozenInstanceError):
        response.content = "Updated"  # type: ignore[misc]
