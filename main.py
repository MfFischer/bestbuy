import products
import promotions
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

best_buy = store.Store(product_list)

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half Price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def start(store):
    """
    Starts the user interface for the store.
    """
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
            # List all products in the store
            products = store.get_all_products()
            print("------")
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show()}")
            print("------")

        elif choice == '2':
            # Show the total quantity of all products in the store
            total_quantity = store.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == '3':
            # Make an order
            shopping_list = []
            while True:
                products = store.get_all_products()
                for idx, product in enumerate(products, 1):
                    print(f"{idx}. {product.show()}")

                try:
                    product_choice = int(input("Select the product number to buy or type '0' to exit: "))
                    if product_choice == 0:
                        break  # Exit the product selection loop
                    if not (1 <= product_choice <= len(products)):
                        print("Invalid product number, please try again.")
                        continue

                    product = products[product_choice - 1]
                    while True:
                        try:
                            quantity = int(
                                input(f"Enter quantity for {product.name} (available: {product.get_quantity()}): "))
                            if quantity <= 0:
                                print("Quantity must be greater than zero.")
                                continue

                            # Check if the quantity is available
                            if quantity > product.get_quantity():
                                print(f"Not enough stock. Available quantity: {product.get_quantity()}")
                                continue

                            # Add product to the shopping list
                            shopping_list.append((product, quantity))
                            break  # Exit the quantity input loop on successful input
                        except ValueError:
                            print("Invalid input, please enter a number.")

                except ValueError:
                    print("Invalid input, please enter a number.")

            if shopping_list:
                try:
                    # Place the order and display the total price
                    total_price = store.order(shopping_list)
                    print(f"Order placed successfully. Total price: ${total_price}")
                except Exception as e:
                    print(f"Error: {e}")

            # Ask user if they want to go back to the menu
            while True:
                back_to_menu = input("Do you want to go back to the menu? (yes/no): ").strip().lower()
                if back_to_menu in ["yes", "no"]:
                    break
                else:
                    print("Invalid input, please type 'yes' or 'no'.")

            if back_to_menu == "yes":
                continue
            else:
                print("Goodbye!")
                break

        elif choice == '4':
            # Quit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)
