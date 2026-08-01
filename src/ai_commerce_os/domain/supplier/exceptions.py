class SupplierError(Exception):
    """Base error for supplier domain interactions."""


class SupplierAuthenticationError(SupplierError):
    """Raised when supplier authentication fails."""


class SupplierConnectionError(SupplierError):
    """Raised when a supplier cannot be reached."""


class SupplierRateLimitError(SupplierError):
    """Raised when a supplier rejects a request due to rate limiting."""


class SupplierNotFoundError(SupplierError):
    """Raised when a supplier resource is not found."""
