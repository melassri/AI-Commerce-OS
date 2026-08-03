from datetime import UTC, datetime
from time import perf_counter
from uuid import uuid4

from ai_commerce_os.core.agent import Agent
from ai_commerce_os.core.runtime.context import RuntimeContext
from ai_commerce_os.core.runtime.exceptions import InvalidAgentError, InvalidTaskError
from ai_commerce_os.core.runtime.result import AgentResult
from ai_commerce_os.core.task import Task


class AgentRuntime:
    """Execute agents synchronously and capture reusable execution metadata."""

    def execute(self, agent: Agent, task: Task) -> AgentResult:
        """Validate inputs, execute an agent, and return its result."""
        self._validate_agent(agent)
        self._validate_task(task)

        context = RuntimeContext(
            execution_id=str(uuid4()),
            started_at=datetime.now(UTC),
            metadata={"agent_id": agent.id, "task_id": task.id},
        )
        started_at = perf_counter()
        try:
            output = agent.execute(task)
        except Exception as error:
            return AgentResult(
                success=False,
                output=None,
                errors=(f"{type(error).__name__}: {error}",),
                duration_ms=(perf_counter() - started_at) * 1000,
                metadata=self._result_metadata(context),
            )

        return AgentResult(
            success=True,
            output=output,
            errors=(),
            duration_ms=(perf_counter() - started_at) * 1000,
            metadata=self._result_metadata(context),
        )

    @staticmethod
    def _validate_agent(agent: Agent) -> None:
        if not isinstance(agent, Agent):
            raise InvalidAgentError("Agent must implement the Agent contract.")

    @staticmethod
    def _validate_task(task: Task) -> None:
        if not isinstance(task, Task):
            raise InvalidTaskError("Task must implement the Task contract.")

    @staticmethod
    def _result_metadata(context: RuntimeContext) -> dict[str, object]:
        return {
            "execution_id": context.execution_id,
            "started_at": context.started_at.isoformat(),
            **context.metadata,
        }
