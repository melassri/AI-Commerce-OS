from abc import ABC, abstractmethod
from collections.abc import Sequence

from ai_commerce_os.domain.supplier.models import SupplierCategory, SupplierProduct


class SupplierConnector(ABC):
    """Port implemented by future supplier-specific infrastructure adapters."""

    @abstractmethod
    def health_check(self) -> bool:
        """Check whether the supplier integration is available."""
        ...

    @abstractmethod
    def search_products(self, query: str) -> Sequence[SupplierProduct]:
        """Search the supplier catalogue."""
        ...

    @abstractmethod
    def get_product(self, supplier_id: str) -> SupplierProduct:
        """Retrieve one supplier product by its supplier identifier."""
        ...

    @abstractmethod
    def get_categories(self) -> Sequence[SupplierCategory]:
        """Retrieve supplier categories."""
        ...

    @abstractmethod
    def validate_credentials(self) -> bool:
        """Validate credentials configured for the supplier integration."""
        ...
