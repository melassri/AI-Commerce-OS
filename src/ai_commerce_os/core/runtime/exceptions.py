class RuntimeError(Exception):
    """Base error raised by runtime validation."""


class InvalidTaskError(RuntimeError):
    """Raised when a runtime execution receives an invalid task."""


class InvalidAgentError(RuntimeError):
    """Raised when a runtime execution receives an invalid agent."""
