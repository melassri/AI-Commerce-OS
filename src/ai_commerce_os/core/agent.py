from abc import ABC, abstractmethod
from collections.abc import Sequence

from ai_commerce_os.core.task import Task


class Agent(ABC):
    """Base contract shared by every AI-Commerce-OS agent."""

    def __init__(
        self,
        agent_id: str,
        name: str,
        description: str,
        objectives: Sequence[str],
        allowed_tools: Sequence[str],
    ) -> None:
        self.id = agent_id
        self.name = name
        self.description = description
        self.objectives = tuple(objectives)
        self.allowed_tools = tuple(allowed_tools)

    @abstractmethod
    def execute(self, task: Task) -> object:
        """Execute a task using the agent's allowed capabilities."""
        ...
