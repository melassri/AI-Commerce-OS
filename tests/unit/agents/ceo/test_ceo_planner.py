import inspect

from ai_commerce_os.agents.ceo.planner import Planner


def test_planner_is_abstract() -> None:
    assert inspect.isabstract(Planner)
