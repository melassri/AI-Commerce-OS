class AgentError(Exception):
    """Base error raised by agent core operations."""


class ToolError(Exception):
    """Base error raised by tool operations."""


class MemoryError(Exception):
    """Base error raised by memory operations."""
