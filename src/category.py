class Category:
    """
    Класс, представляющий категорию товаров.
    """

    category_count = 0

    def __init__(self, name, description, products):
        """
        Инициализация новой категории.

        Параметры:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список продуктов в категории.
        """
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = len(products)
        Category.category_count += 1

    @classmethod
    def reset_counts(cls):
        """
        Сброс общего количества категорий и продуктов.
        """
        cls.category_count = 0

    def add_product(self, product):
        """
        Добавление продукта в категорию.

        Параметры:
            product (Product): Продукт, который нужно добавить в категорию.
        """
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        """
        Получение строкового представления всех продуктов в категории.

        Возвращает:
            str: Строка с информацией о каждом продукте в категории,
                 включая название, цену и остаток на складе.
        """
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )
