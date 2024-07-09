from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the promotion to the given product and quantity.
        """
        pass


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage discount to the product.
    """

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = (self.percent / 100) * product.price
        return product.price * quantity - discount * quantity


class SecondHalfPrice(Promotion):
    """
    Promotion that makes every second item half price.
    """

    def apply_promotion(self, product, quantity) -> float:
        if quantity < 2:
            return product.price * quantity
        full_price_count = quantity // 2 + quantity % 2
        half_price_count = quantity // 2
        return (full_price_count * product.price) + (half_price_count * product.price * 0.5)


class ThirdOneFree(Promotion):
    """
    Promotion that makes every third item free.
    """

    def apply_promotion(self, product, quantity) -> float:
        if quantity < 3:
            return product.price * quantity
        full_price_count = quantity - (quantity // 3)
        return full_price_count * product.price
