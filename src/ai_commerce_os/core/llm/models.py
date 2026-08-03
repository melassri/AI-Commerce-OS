from collections.abc import Mapping
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class LLMMessage:
    """An immutable message exchanged with an LLM provider."""

    role: str
    content: str


@dataclass(frozen=True, slots=True)
class LLMResponse:
    """An immutable response returned by an LLM provider."""

    content: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    metadata: Mapping[str, object] = field(default_factory=dict)
