import inspect

from ai_commerce_os.core.tool import Tool


class ExampleTool(Tool):
    @property
    def name(self) -> str:
        return "example-tool"

    def execute(self) -> object:
        return "completed"


def test_tool_is_abstract() -> None:
    assert inspect.isabstract(Tool)


def test_tool_exposes_name_and_executes() -> None:
    tool = ExampleTool()

    assert tool.name == "example-tool"
    assert tool.execute() == "completed"
