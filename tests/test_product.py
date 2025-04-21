import pytest
from src.product import Product


@pytest.mark.parametrize("product_data, expected_name, expected_description", [
    ({"name": "Тестовый продукт 1", "description": "Описание продукта 1", "price": 100.0, "quantity": 10},
     "Тестовый продукт 1", "Описание продукта 1"),
    ({"name": "Тестовый продукт 2", "description": "Описание продукта 2", "price": 200.0, "quantity": 5},
     "Тестовый продукт 2", "Описание продукта 2"),
])
def test_new_product(product_data, expected_name, expected_description):
    product = Product.new_product(product_data)
    assert product.name == expected_name
    assert product.description == expected_description


@pytest.mark.parametrize("initial_price, new_price, expected_price", [
    (100.0, 150.0, 150.0),
    (200.0, -50.0, 200.0),
])
def test_price_setter(initial_price, new_price, expected_price):
    product = Product("Тестовый продукт", "Описание продукта", initial_price, 10)
    product.price = new_price
    assert product.price == expected_price
