import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(store):
    while True:
        print("""
        Store Menu
        ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """)
        choice = input("Please choose a number: ")

        if choice == '1':
            products = store.get_all_products()
            print("------")
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show()}")
            print("------")

        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == '3':
            shopping_list = []
            while True:
                products = store.get_all_products()
                for idx, product in enumerate(products, 1):
                    print(f"{idx}. {product.show()}")

                try:
                    product_choice = int(input("Select the product number to buy (0 to finish): "))
                    if product_choice == 0:
                        break
                    if not (1 <= product_choice <= len(products)):
                        print("Invalid product number, please try again.")
                        continue

                    product = products[product_choice - 1]
                    quantity = int(input(f"Enter quantity for {product.name}: "))
                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                        continue

                    shopping_list.append((product, quantity))
                except ValueError:
                    print("Invalid input, please enter a number.")

            try:
                total_price = store.order(shopping_list)
                print(f"Order placed successfully. Total price: ${total_price}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)
