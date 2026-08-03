import pytest

from ai_commerce_os.core.agent import Agent
from ai_commerce_os.core.exceptions import AgentError
from ai_commerce_os.core.registry import AgentRegistry
from ai_commerce_os.core.task import Task


class ExampleAgent(Agent):
    def execute(self, task: Task) -> object:
        return task


def create_agent(agent_id: str) -> ExampleAgent:
    return ExampleAgent(
        agent_id=agent_id,
        name="Example Agent",
        description="An example agent.",
        objectives=[],
        allowed_tools=[],
    )


def test_registry_registers_and_resolves_agents() -> None:
    registry = AgentRegistry()
    agent = create_agent("agent-1")

    registry.register_agent(agent)

    assert registry.get_agent("agent-1") is agent
    assert registry.list_agents() == [agent]


def test_registry_returns_none_for_unknown_agent() -> None:
    assert AgentRegistry().get_agent("unknown") is None


def test_registry_rejects_duplicate_agent_identifiers() -> None:
    registry = AgentRegistry()
    registry.register_agent(create_agent("agent-1"))

    with pytest.raises(AgentError, match="already registered"):
        registry.register_agent(create_agent("agent-1"))
