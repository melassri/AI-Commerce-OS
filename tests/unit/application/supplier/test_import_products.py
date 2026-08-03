from collections.abc import Sequence
from decimal import Decimal

import pytest

from ai_commerce_os.application.supplier.import_products import (
    ImportSupplierProductsUseCase,
)
from ai_commerce_os.domain.supplier.exceptions import SupplierConnectionError
from ai_commerce_os.domain.supplier.models import SupplierCategory, SupplierProduct
from ai_commerce_os.domain.supplier.ports import SupplierConnector


class StubSupplierConnector(SupplierConnector):
    def __init__(
        self,
        products: Sequence[SupplierProduct],
        error: SupplierConnectionError | None = None,
    ) -> None:
        self.products = products
        self.error = error
        self.queries: list[str] = []

    def health_check(self) -> bool:
        return True

    def search_products(self, query: str) -> Sequence[SupplierProduct]:
        self.queries.append(query)
        if self.error is not None:
            raise self.error
        return self.products

    def get_product(self, supplier_id: str) -> SupplierProduct:
        raise NotImplementedError

    def get_categories(self) -> Sequence[SupplierCategory]:
        return []

    def validate_credentials(self) -> bool:
        return True


def create_supplier_product() -> SupplierProduct:
    return SupplierProduct(
        supplier_id="supplier-product-1",
        supplier_name="Example Supplier",
        title="Example Product",
        description=None,
        price=Decimal("19.99"),
        currency="EUR",
        stock=12,
        category=None,
        brand=None,
    )


def test_execute_calls_connector_once() -> None:
    connector = StubSupplierConnector([create_supplier_product()])
    use_case = ImportSupplierProductsUseCase(connector)

    use_case.execute("example")

    assert connector.queries == ["example"]


def test_execute_propagates_returned_products_unchanged() -> None:
    products = [create_supplier_product()]
    use_case = ImportSupplierProductsUseCase(StubSupplierConnector(products))

    result = use_case.execute("example")

    assert result == products
    assert result[0] is products[0]


def test_execute_propagates_supplier_errors() -> None:
    error = SupplierConnectionError("Supplier is unavailable")
    use_case = ImportSupplierProductsUseCase(StubSupplierConnector([], error=error))

    with pytest.raises(SupplierConnectionError) as error_info:
        use_case.execute("example")

    assert error_info.value is error
