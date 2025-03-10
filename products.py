class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # New instance variable for promotion

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product. Deactivates the product if the quantity is zero.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check if the product is active.
        """
        return self.active

    def activate(self):
        """
        Activate the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False

    def set_promotion(self, promotion):
        """
        Set a promotion for the product.
        """
        self.promotion = promotion

    def show(self) -> str:
        """
        Show the product details, including the promotion if it exists.
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity) -> float:
        """
        Buy a certain quantity of the product.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available quantity: {self.quantity}")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """Represents a product that does not have stock quantity."""

    def __init__(self, name, price):
        """Initialize the non-stocked product with name and price."""
        super().__init__(name, price, 0)  # Set quantity to 0

    @property
    def quantity(self):
        """Return an infinite quantity for non-stocked products."""
        return float('inf')

    @quantity.setter
    def quantity(self, value):
        """Do nothing since quantity is always infinite."""
        pass

    def buy(self, quantity):
        """Process the purchase of a non-stocked product."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if self.promotion:  # Use the property method for promotion
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def __str__(self):
        """Return a string representation of the non-stocked product."""
        return f"{self.name}, Price: ${self.price} (Non-stocked product)"


class LimitedProduct(Product):
    """
    Represents a limited product. There is a maximum purchase limit per order.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        """
        Buy a certain quantity of the product.
        Ensures quantity does not exceed the maximum limit.
        """
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} items at a time")
        return super().buy(quantity)

    def show(self) -> str:
        """
        Show the product details, including the promotion if it exists.
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (f"{self.name} (Limited, Max {self.maximum} per order), "
                f"Price: {self.price}, Quantity: {self.quantity}{promotion_info}")
