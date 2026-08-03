from ai_commerce_os.agents.ceo.models import Plan, PlannedTask
from ai_commerce_os.agents.ceo.planner import Planner
from ai_commerce_os.core.agent import Agent
from ai_commerce_os.core.task import Task


class CEOAgent(Agent):
    """Delegate objective planning and task assignment to a planner."""

    def __init__(self, planner: Planner) -> None:
        super().__init__(
            agent_id="ceo",
            name="CEO",
            description="Plans objectives and delegates tasks to specialized agents.",
            objectives=("Understand objectives", "Plan work", "Delegate tasks"),
            allowed_tools=(),
        )
        self._planner = planner

    def create_plan(self, goal: str) -> Plan:
        """Delegate plan creation to the configured planner."""
        return self._planner.create_plan(goal)

    def choose_agent(self, task: PlannedTask) -> str:
        """Return the agent already assigned by the plan."""
        return task.assigned_agent

    def execute(self, task: Task) -> Plan:
        """Delegate a task objective to the planner without performing work."""
        return self.create_plan(task.description)
