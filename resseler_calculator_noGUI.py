class CosmeticItem:
    def __init__(self, name, cost_price):
        self.name = name
        self.cost_price = cost_price

    def calculate_selling_price(self):
        return self.cost_price * 1.10

    def format_price(self, price):
        return "{:,.0f}".format(price).replace(",", ".")

def main():
    items = []
    while True:
        print("\nWelcome!..Siti! let me help you with the price sell of your product!")
        name = input("Enter the name of the cosmetic item (or 'exit' to stop): ")
        if name.lower() == 'exit':
            print("Thank You, wish the best for your bussiness! See You")
            break
        cost_price = float(input("Enter the cost price of the item: "))
        item = CosmeticItem(name, cost_price)
        items.append(item)

        print("\nSelling Prices:")
        for item in items:
            print(f"{item.name}: {item.format_price(item.calculate_selling_price())}")
        print("\n")

if __name__ == "__main__":
    main()
