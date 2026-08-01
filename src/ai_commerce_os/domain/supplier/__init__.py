"""Supplier domain contracts for future infrastructure adapters."""

from ai_commerce_os.domain.supplier.exceptions import (
    SupplierAuthenticationError,
    SupplierConnectionError,
    SupplierError,
    SupplierNotFoundError,
    SupplierRateLimitError,
)
from ai_commerce_os.domain.supplier.models import SupplierCategory, SupplierProduct
from ai_commerce_os.domain.supplier.ports import SupplierConnector

__all__ = [
    "SupplierAuthenticationError",
    "SupplierCategory",
    "SupplierConnectionError",
    "SupplierConnector",
    "SupplierError",
    "SupplierNotFoundError",
    "SupplierProduct",
    "SupplierRateLimitError",
]
