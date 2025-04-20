import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.reset_counts()


@pytest.mark.parametrize("name, description, price, quantity", [
    ("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
    ("Iphone 15", "512GB, Gray space", 210000.0, 8),
    ("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
])
def test_product_creation(name, description, price, quantity):
    product = Product(name, description, price, quantity)
    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


@pytest.mark.parametrize("category_name, category_description, products_data", [
    (
        "Смартфоны",
        "Смартфоны как средство не только коммуникации.",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB...", 180000.0, 5),
            Product("Iphone 15", "512GB...", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB...", 31000.0, 14)
        ]
    ),
    (
        "Телевизоры",
        "Современный телевизор.",
        [
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )
])
def test_category_creation(category_name, category_description, products_data):
    category = Category(category_name, category_description, products_data)
    assert category.name == category_name
    assert category.description == category_description
    assert len(category.products) == len(products_data)


def test_category_counts():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB...", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB...", 210000.0, 8)
    Category("Смартфоны", "Описание смартфонов.", [product1])
    Category("Телевизоры", "Описание телевизоров.", [product2])
    assert Category.category_count == 2
