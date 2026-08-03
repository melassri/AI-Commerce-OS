from dataclasses import FrozenInstanceError

import pytest

from ai_commerce_os.core.task import Task


def test_task_is_created_with_defaults() -> None:
    task = Task(id="task-1", title="Example", description="Example task")

    assert task.priority == 0
    assert task.status == "pending"
    assert task.payload == {}


def test_task_is_immutable() -> None:
    task = Task(id="task-1", title="Example", description="Example task")

    with pytest.raises(FrozenInstanceError):
        task.status = "completed"  # type: ignore[misc]
