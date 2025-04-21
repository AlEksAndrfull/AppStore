import pytest
from src.category import Category
from src.product import Product


@pytest.mark.parametrize("products_data, expected_count", [
    ([Product("Product A", "Description A", 50.0, 5),
      Product("Product B", "Description B", 75.0, 3)], 2),
    ([Product("Product C", "Description C", 100.0, 10)], 1),
])
def test_category_initialization(products_data, expected_count):
    category = Category("Test Category", "Test Description", products_data)

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == expected_count
