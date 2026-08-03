from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PlannedTask:
    """An immutable task assignment proposed by a planner."""

    id: str
    title: str
    description: str
    assigned_agent: str


@dataclass(frozen=True, slots=True)
class Plan:
    """An immutable plan for delegating work to agents."""

    id: str
    goal: str
    tasks: tuple[PlannedTask, ...]
