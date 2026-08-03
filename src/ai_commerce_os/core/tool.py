from abc import ABC, abstractmethod


class Tool(ABC):
    """A capability made available to an agent."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the tool's stable name."""
        ...

    @abstractmethod
    def execute(self) -> object:
        """Execute the tool operation."""
        ...
