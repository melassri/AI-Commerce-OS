from ai_commerce_os.domain.supplier.models import SupplierProduct
from ai_commerce_os.domain.supplier.ports import SupplierConnector


class ImportSupplierProductsUseCase:
    """Delegate supplier product imports to the configured connector."""

    def __init__(self, connector: SupplierConnector) -> None:
        self._connector = connector

    def execute(self, query: str) -> list[SupplierProduct]:
        """Import products returned by the supplier connector for a query."""
        return list(self._connector.search_products(query))
