from decimal import Decimal

from ai_commerce_os.domain.supplier.models import SupplierCategory, SupplierProduct


def test_supplier_product_creation() -> None:
    product = SupplierProduct(
        supplier_id="supplier-product-1",
        supplier_name="Example Supplier",
        title="Example Product",
        description="An example supplier product.",
        price=Decimal("19.99"),
        currency="EUR",
        stock=12,
        category="Example category",
        brand="Example brand",
        images=("https://example.test/product.jpg",),
        attributes={"color": "blue"},
        source_url="https://example.test/products/supplier-product-1",
    )

    assert product.supplier_id == "supplier-product-1"
    assert product.price == Decimal("19.99")
    assert product.images == ("https://example.test/product.jpg",)


def test_supplier_category_creation() -> None:
    category = SupplierCategory(
        supplier_id="supplier-category-1",
        supplier_name="Example Supplier",
        category_id="category-1",
        name="Example category",
    )

    assert category.category_id == "category-1"
    assert category.parent_id is None
