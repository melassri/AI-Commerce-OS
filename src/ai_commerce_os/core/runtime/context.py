from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, slots=True)
class RuntimeContext:
    """Immutable metadata captured when an agent execution starts."""

    execution_id: str
    started_at: datetime
    metadata: Mapping[str, object] = field(default_factory=dict)
