import pytest
from src.product import Product


@pytest.mark.parametrize("product_name, expected_str", [
    ("Samsung Galaxy S23 Ultra", "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."),
    ("Iphone 15", "Iphone 15, 210000.0 руб. Остаток: 8 шт."),
])
def test_product_str(product_name, expected_str):
    """
    Тестирует строковое представление продукта.

    :param product_name: Название тестируемого продукта.
    :param expected_str: Ожидаемая строка для сравнения.
    """
    product = Product(
        product_name,
        "Описание",
        180000.0 if product_name == "Samsung Galaxy S23 Ultra" else 210000.0,
        5 if product_name == "Samsung Galaxy S23 Ultra" else 8
    )
    assert str(product) == expected_str


@pytest.mark.parametrize(
    "product_a_price, product_a_quantity, product_b_price, product_b_quantity, expected_sum",
    [
        (180000.0, 5, 210000.0, 8, (180000.0 * 5) + (210000.0 * 8)),
        (31000.0, 14, 20000.0, 10, (31000.0 * 14) + (20000.0 * 10)),
    ]
)
def test_product_add(
    product_a_price,
    product_a_quantity,
    product_b_price,
    product_b_quantity,
    expected_sum
):
    """
    Тестирует сложение двух продуктов.

    :param product_a_price: Цена первого продукта.
    :param product_a_quantity: Количество первого продукта.
    :param product_b_price: Цена второго продукта.
    :param product_b_quantity: Количество второго продукта.
    :param expected_sum: Ожидаемая сумма стоимости двух продуктов.
    """
    product_a = Product("Product A", "Описание A", product_a_price, product_a_quantity)
    product_b = Product("Product B", "Описание B", product_b_price, product_b_quantity)

    assert (product_a + product_b) == expected_sum
