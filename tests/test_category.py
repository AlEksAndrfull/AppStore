import pytest
from src.category import Category
from src.product import Product


@pytest.mark.parametrize("products, expected_str", [
    (
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ],
        "Смартфоны, количество продуктов: 27 шт."
    ),
    (
        [
            Product("MacBook Pro", "16GB RAM, 512GB SSD", 150000.0, 3),
            Product("Dell XPS 13", "16GB RAM, 256GB SSD", 120000.0, 2)
        ],
        "Ноутбуки, количество продуктов: 5 шт."
    )
])
def test_category_str(products, expected_str):
    """
    Тестирует строковое представление категории продуктов.

    :param products: Список продуктов в категории.
    :param expected_str: Ожидаемая строка для сравнения.
    """
    category = Category("Смартфоны" if len(products) == 3 else "Ноутбуки", "Описание категории", products)
    assert str(category) == expected_str
