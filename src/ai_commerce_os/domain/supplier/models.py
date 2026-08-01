from collections.abc import Mapping
from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class SupplierProduct:
    """Framework-independent product data supplied by a connector."""

    supplier_id: str
    supplier_name: str
    title: str
    description: str | None
    price: Decimal
    currency: str
    stock: int
    category: str | None
    brand: str | None
    images: tuple[str, ...] = ()
    attributes: Mapping[str, str] = field(default_factory=dict)
    source_url: str | None = None


@dataclass(frozen=True, slots=True)
class SupplierCategory:
    """Framework-independent category data supplied by a connector."""

    supplier_id: str
    supplier_name: str
    category_id: str
    name: str
    parent_id: str | None = None
