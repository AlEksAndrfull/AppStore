class Product:
    """Класс, представляющий продукт."""

    def __init__(self, name, description, price, quantity):
        """
        Инициализация продукта.

        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение двух продуктов.

        :param other: Другой продукт для сложения.
        :return: Сумма стоимости двух продуктов.
        """
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented
