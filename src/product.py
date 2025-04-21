class Product:
    """
    Класс, представляющий продукт.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        __price (float): Цена продукта (приватный атрибут).
        quantity (int): Количество продукта на складе.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализация нового продукта.

        Параметры:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """
        Получение цены продукта.

        Возвращает:
            float: Цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Установка новой цены для продукта.

        Параметры:
            new_price (float): Новая цена продукта.

        Если новая цена меньше или равна нулю, выводится сообщение об ошибке.
        """
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict):
        """
        Создание нового экземпляра продукта из словаря.

        Параметры:
            product_dict (dict): Словарь с данными о продукте.
                                 Должен содержать ключи: "name", "description", "price", "quantity".

        Возвращает:
            Product: Новый экземпляр класса Product.
        """
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"]
        )
