from typing import cast

import pytest

from ai_commerce_os.core.agent import Agent
from ai_commerce_os.core.runtime.exceptions import InvalidAgentError, InvalidTaskError
from ai_commerce_os.core.runtime.runtime import AgentRuntime
from ai_commerce_os.core.task import Task


class SuccessfulAgent(Agent):
    def execute(self, task: Task) -> object:
        return {"task_id": task.id}


class FailingAgent(Agent):
    def execute(self, task: Task) -> object:
        raise ValueError("Execution failed")


def create_agent(agent_type: type[Agent]) -> Agent:
    return agent_type(
        agent_id="agent-1",
        name="Example Agent",
        description="An example agent.",
        objectives=[],
        allowed_tools=[],
    )


def create_task() -> Task:
    return Task(id="task-1", title="Example", description="Example task")


def test_runtime_returns_successful_agent_result() -> None:
    result = AgentRuntime().execute(create_agent(SuccessfulAgent), create_task())

    assert result.success is True
    assert result.output == {"task_id": "task-1"}
    assert result.errors == ()
    assert result.duration_ms >= 0
    assert result.metadata["agent_id"] == "agent-1"
    assert result.metadata["task_id"] == "task-1"
    assert "execution_id" in result.metadata
    assert "started_at" in result.metadata


def test_runtime_rejects_invalid_agent() -> None:
    with pytest.raises(InvalidAgentError, match="Agent must implement"):
        AgentRuntime().execute(cast(Agent, object()), create_task())


def test_runtime_rejects_invalid_task() -> None:
    with pytest.raises(InvalidTaskError, match="Task must implement"):
        AgentRuntime().execute(create_agent(SuccessfulAgent), cast(Task, object()))


def test_runtime_returns_failed_agent_result() -> None:
    result = AgentRuntime().execute(create_agent(FailingAgent), create_task())

    assert result.success is False
    assert result.output is None
    assert result.errors == ("ValueError: Execution failed",)
    assert result.duration_ms >= 0
