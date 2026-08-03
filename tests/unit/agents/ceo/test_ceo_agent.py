from ai_commerce_os.agents.ceo.agent import CEOAgent
from ai_commerce_os.agents.ceo.models import Plan, PlannedTask
from ai_commerce_os.agents.ceo.planner import Planner
from ai_commerce_os.core.task import Task


class StubPlanner(Planner):
    def __init__(self, plan: Plan) -> None:
        self.plan = plan
        self.goals: list[str] = []

    def create_plan(self, goal: str) -> Plan:
        self.goals.append(goal)
        return self.plan


def create_plan() -> Plan:
    return Plan(
        id="plan-1",
        goal="Example goal",
        tasks=(
            PlannedTask(
                id="planned-task-1",
                title="Example",
                description="Example task.",
                assigned_agent="scout",
            ),
        ),
    )


def test_ceo_agent_has_fixed_identity() -> None:
    agent = CEOAgent(StubPlanner(create_plan()))

    assert agent.id == "ceo"
    assert agent.name == "CEO"
    assert agent.allowed_tools == ()


def test_ceo_agent_delegates_plan_creation_and_task_assignment() -> None:
    plan = create_plan()
    planner = StubPlanner(plan)
    agent = CEOAgent(planner)

    assert agent.create_plan("Example goal") is plan
    assert agent.choose_agent(plan.tasks[0]) == "scout"
    assert planner.goals == ["Example goal"]


def test_ceo_agent_execute_delegates_task_objective_to_planner() -> None:
    plan = create_plan()
    planner = StubPlanner(plan)
    agent = CEOAgent(planner)
    task = Task(id="task-1", title="Example", description="Objective to plan")

    assert agent.execute(task) is plan
    assert planner.goals == ["Objective to plan"]
