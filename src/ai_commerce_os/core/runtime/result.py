from collections.abc import Mapping
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class AgentResult:
    """Immutable outcome of a synchronous agent execution."""

    success: bool
    output: object | None
    errors: tuple[str, ...]
    duration_ms: float
    metadata: Mapping[str, object] = field(default_factory=dict)
