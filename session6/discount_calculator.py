def calculate_discounted_price(purchase_amount):
    if purchase_amount > 100:
        discount = 0.10
    elif 50 < purchase_amount <= 100:
        discount = 0.05
    else:
        discount = 0

    discounted_price = purchase_amount * (1 - discount)
    return discounted_price

def main():
    try:
        items = {}  # Dictionary to store product names and amounts
        total_cost = 0

        while True:
            product_name = input("Enter the name of the product (or 'done' to finish): ")
            if product_name.lower() == "done":
                break

            try:
                item_cost = float(input(f"Enter the cost of '{product_name}' ($): "))
                if item_cost < 0:
                    print("Invalid input. Please enter a positive amount.")
                    continue

                item_amount = int(input(f"Enter the quantity of '{product_name}': "))
                if item_amount < 0:
                    print("Invalid input. Please enter a positive quantity.")
                    continue

                items[product_name] = item_cost * item_amount
                total_cost += items[product_name]
            except ValueError:
                print("Invalid input. Please enter valid numeric values.")

        final_price = calculate_discounted_price(total_cost)
        discount_amount = total_cost - final_price

        print("\nReceipt Summary:")
        print(f"Total items purchased: {len(items)}")
        for product, cost in items.items():
            print(f"{product}: ${cost:.2f}")
        print(f"Total cost before discount: ${total_cost:.2f}")
        print(f"Discount applied: ${discount_amount:.2f}")
        print(f"Total cost after discount: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
