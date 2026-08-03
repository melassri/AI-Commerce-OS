import pytest

from ai_commerce_os.core.exceptions import AgentError, MemoryError, ToolError


@pytest.mark.parametrize("exception_type", [AgentError, ToolError, MemoryError])
def test_core_exceptions_inherit_from_exception(
    exception_type: type[Exception],
) -> None:
    assert isinstance(exception_type(), Exception)
