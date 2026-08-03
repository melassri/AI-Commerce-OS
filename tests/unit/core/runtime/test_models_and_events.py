from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

import pytest

from ai_commerce_os.core.runtime.context import RuntimeContext
from ai_commerce_os.core.runtime.events import AgentCompleted, AgentFailed, AgentStarted
from ai_commerce_os.core.runtime.result import AgentResult


def create_context() -> RuntimeContext:
    return RuntimeContext(
        execution_id="execution-1",
        started_at=datetime(2026, 8, 3, tzinfo=UTC),
        metadata={"agent_id": "agent-1"},
    )


def create_result() -> AgentResult:
    return AgentResult(
        success=True,
        output="result",
        errors=(),
        duration_ms=10.0,
        metadata={"task_id": "task-1"},
    )


def test_runtime_context_is_immutable() -> None:
    context = create_context()

    assert context.execution_id == "execution-1"
    with pytest.raises(FrozenInstanceError):
        context.execution_id = "execution-2"  # type: ignore[misc]


def test_agent_result_is_immutable() -> None:
    result = create_result()

    assert result.success is True
    with pytest.raises(FrozenInstanceError):
        result.success = False  # type: ignore[misc]


def test_runtime_events_are_created() -> None:
    context = create_context()
    result = create_result()

    started = AgentStarted(context=context, agent_id="agent-1", task_id="task-1")
    completed = AgentCompleted(
        context=context,
        agent_id="agent-1",
        task_id="task-1",
        result=result,
    )
    failed = AgentFailed(
        context=context,
        agent_id="agent-1",
        task_id="task-1",
        errors=("ValueError: Execution failed",),
    )

    assert started.context is context
    assert completed.result is result
    assert failed.errors == ("ValueError: Execution failed",)
