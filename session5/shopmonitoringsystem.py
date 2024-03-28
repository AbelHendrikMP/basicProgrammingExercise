class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Store:
    def __init__(self):
        self.inventory = []
        self.transactions = 0
        self.profits = 0

    def add_item(self, name, price, stock):
        self.inventory.append(Item(name, price, stock))

    def purchase_item(self, name, quantity):
        for item in self.inventory:
            if item.name == name:
                if item.stock >= quantity:
                    item.stock -= quantity
                    self.transactions += quantity
                    self.profits += item.price * quantity
                    print(f"Purchased {quantity} {item.name}(s) for {item.price * quantity}. Remaining stock: {item.stock}")
                else:
                    print("Sorry, we don't have enough stock for that item.")
                return
        print("Sorry, we don't have that item.")

    def report(self):
        print(f"Total transactions: {self.transactions}")
        print(f"Total profits: {self.profits}")

# Example usage:
store = Store()

while True:
    print("1. Add item")
    print("2. Purchase item")
    print("3. Report")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        stock = int(input("Enter item stock: "))
        store.add_item(name, price, stock)
    elif choice == 2:
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        store.purchase_item(name, quantity)
    elif choice == 3:
        store.report()
    elif choice == 4:
        print("thank you for your work hard, see you!")
        break
    else:
        print("Invalid choice. Please try again.")
