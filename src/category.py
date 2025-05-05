class Category:
    """Класс, представляющий категорию продуктов."""

    def __init__(self, name, description, products):
        """
        Инициализация категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список продуктов в категории.
        """
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
