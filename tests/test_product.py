import pytest
from src.product import Product


@pytest.mark.parametrize("name, description, price, quantity", [
    ("Test Product 1", "Test Description 1", 100.0, 10),
    ("Test Product 2", "Test Description 2", 200.0, 5),
    ("Test Product 3", "Test Description 3", 150.0, 20),
])
def test_product_initialization(name, description, price, quantity):
    product = Product(name, description, price, quantity)
    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity
