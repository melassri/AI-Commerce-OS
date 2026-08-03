from abc import ABC, abstractmethod


class Memory(ABC):
    """Storage contract for agent memory implementations."""

    @abstractmethod
    def store(self, key: str, value: object) -> None:
        """Store a value under a stable key."""
        ...

    @abstractmethod
    def retrieve(self, key: str) -> object | None:
        """Retrieve a value by key when it exists."""
        ...
