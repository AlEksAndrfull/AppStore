class Category:
    """
    Класс для представления категории продуктов.

    Атрибуты:
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество продуктов во всех категориях.

    Методы:
        __init__(name: str, description: str, products: list):
            Инициализирует объект категории с заданным именем, описанием и списком продуктов.
        reset_counts():
            Сбрасывает счетчики категорий и продуктов.
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализирует объект категории.

        Параметры:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список продуктов, принадлежащих этой категории.

        Увеличивает счетчик категорий и счетчик продуктов на основе переданного списка.
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @classmethod
    def reset_counts(cls):
        """Сбрасывает счетчики категорий и продуктов."""
        cls.category_count = 0
        cls.product_count = 0
