class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes the product with a name, price, and quantity.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Returns the current quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets the quantity and deactivates if it reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Checks if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity, returns the total price.
        Raises Exception if the product is not active or not enough quantity.
        """
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    Represents a non-stocked product in the store.
    Non-stocked products do not have a quantity.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes the non-stocked product with a name and price.
        Quantity is set to 0 and remains unchanged.
        """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Overrides the set_quantity method to do nothing."""
        pass

    def show(self) -> str:
        """Returns a string representation of the non-stocked product."""
        return f"{self.name}, Price: {self.price}, Quantity: N/A"


class LimitedProduct(Product):
    """
    Represents a limited product in the store.
    Limited products have a maximum quantity that can be purchased in one order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initializes the limited product with a name, price, quantity, and maximum quantity per order.
        """
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum quantity must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity, returns the total price.
        Raises Exception if the quantity exceeds the maximum allowed per order.
        """
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} units in one order.")
        return super().buy(quantity)

    def show(self) -> str:
        """Returns a string representation of the limited product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}"


# Example usage
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    for product in product_list:
        print(product.show())
