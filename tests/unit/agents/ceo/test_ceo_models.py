from dataclasses import FrozenInstanceError

import pytest

from ai_commerce_os.agents.ceo.models import Plan, PlannedTask


def test_planned_task_is_immutable() -> None:
    task = PlannedTask(
        id="planned-task-1",
        title="Example",
        description="Example task.",
        assigned_agent="scout",
    )

    assert task.assigned_agent == "scout"
    with pytest.raises(FrozenInstanceError):
        task.title = "Updated"  # type: ignore[misc]


def test_plan_is_immutable() -> None:
    plan = Plan(id="plan-1", goal="Example goal", tasks=())

    assert plan.tasks == ()
    with pytest.raises(FrozenInstanceError):
        plan.goal = "Updated"  # type: ignore[misc]
