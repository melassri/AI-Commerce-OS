from collections.abc import Mapping
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Task:
    """An immutable request for an agent to execute."""

    id: str
    title: str
    description: str
    priority: int = 0
    status: str = "pending"
    payload: Mapping[str, object] = field(default_factory=dict)
