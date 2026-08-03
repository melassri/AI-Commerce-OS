from abc import ABC, abstractmethod

from ai_commerce_os.agents.ceo.models import Plan


class Planner(ABC):
    """Port for future planning strategies used by the CEO agent."""

    @abstractmethod
    def create_plan(self, goal: str) -> Plan:
        """Create an immutable plan for a goal."""
        ...
