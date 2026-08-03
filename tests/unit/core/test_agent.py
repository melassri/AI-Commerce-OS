import inspect

from ai_commerce_os.core.agent import Agent
from ai_commerce_os.core.task import Task


class ExampleAgent(Agent):
    def execute(self, task: Task) -> object:
        return task


def test_agent_is_abstract() -> None:
    assert inspect.isabstract(Agent)


def test_agent_exposes_configured_metadata() -> None:
    agent = ExampleAgent(
        agent_id="agent-1",
        name="Example Agent",
        description="An example agent.",
        objectives=["Assist"],
        allowed_tools=["example-tool"],
    )
    task = Task(id="task-1", title="Example", description="Example task")

    assert agent.id == "agent-1"
    assert agent.name == "Example Agent"
    assert agent.description == "An example agent."
    assert agent.objectives == ("Assist",)
    assert agent.allowed_tools == ("example-tool",)
    assert agent.execute(task) is task
