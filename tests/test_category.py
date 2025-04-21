import pytest
from src.category import Category
from src.product import Product


def test_add_product():
    category = Category("Тестовая категория", "Описание категории", [])
    product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
    category.add_product(product)
    assert category.product_count == 1


@pytest.mark.parametrize("products_data, expected_output", [
    ([{"name": "Продукт A", "description": "Описание A", "price": 100.0, "quantity": 10},
      {"name": "Продукт B", "description": "Описание B", "price": 200.0, "quantity": 5}],
     "Продукт A, 100.0 руб. Остаток: 10 шт.\nПродукт B, 200.0 руб. Остаток: 5 шт."),
])
def test_products_property(products_data, expected_output):
    category = Category("Тестовая категория", "Описание категории", [])
    for data in products_data:
        product = Product(data["name"], data["description"], data["price"], data["quantity"])
        category.add_product(product)
    assert category.products == expected_output
