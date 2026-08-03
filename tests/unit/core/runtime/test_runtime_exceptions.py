import pytest

from ai_commerce_os.core.runtime.exceptions import (
    InvalidAgentError,
    InvalidTaskError,
    RuntimeError,
)


@pytest.mark.parametrize("exception_type", [InvalidAgentError, InvalidTaskError])
def test_runtime_exceptions_inherit_from_runtime_error(
    exception_type: type[RuntimeError],
) -> None:
    assert isinstance(exception_type(), RuntimeError)
