import inspect

from ai_commerce_os.domain.supplier.ports import SupplierConnector


def test_supplier_connector_is_abstract() -> None:
    assert inspect.isabstract(SupplierConnector)
