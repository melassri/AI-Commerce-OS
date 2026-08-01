import pytest

from ai_commerce_os.domain.supplier.exceptions import (
    SupplierAuthenticationError,
    SupplierConnectionError,
    SupplierError,
    SupplierNotFoundError,
    SupplierRateLimitError,
)


@pytest.mark.parametrize(
    "exception_type",
    [
        SupplierAuthenticationError,
        SupplierConnectionError,
        SupplierRateLimitError,
        SupplierNotFoundError,
    ],
)
def test_supplier_exceptions_inherit_from_supplier_error(
    exception_type: type[SupplierError],
) -> None:
    assert isinstance(exception_type(), SupplierError)
