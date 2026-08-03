from dataclasses import dataclass

from ai_commerce_os.core.runtime.context import RuntimeContext
from ai_commerce_os.core.runtime.result import AgentResult


@dataclass(frozen=True, slots=True)
class AgentStarted:
    """Model an agent execution start without dispatching it."""

    context: RuntimeContext
    agent_id: str
    task_id: str


@dataclass(frozen=True, slots=True)
class AgentCompleted:
    """Model a successful agent execution without dispatching it."""

    context: RuntimeContext
    agent_id: str
    task_id: str
    result: AgentResult


@dataclass(frozen=True, slots=True)
class AgentFailed:
    """Model a failed agent execution without dispatching it."""

    context: RuntimeContext
    agent_id: str
    task_id: str
    errors: tuple[str, ...]
