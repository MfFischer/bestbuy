from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all items in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Processes an order and returns the total price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


# Example usage
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    products_in_store = store.get_all_products()
    print(store.get_total_quantity())  # Should print the total quantity of all products

    order_cost = store.order([(products_in_store[0], 1), (products_in_store[1], 2)])
    print(f"Order cost: {order_cost} dollars.")  # Should print the total price of the order
