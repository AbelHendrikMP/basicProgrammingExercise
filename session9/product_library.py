# Product management program (modified)

def display_menu():
    print("\nMenu:")
    print("1. List products")
    print("2. Add product(s)")
    print("3. Delete product by number")
    print("4. Delete product by name")
    print("5. Exit")

def list_products(products):
    print("\nProducts:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product}")

def add_products(products):
    while True:
        new_product = input("Enter a product name (or 'end' to finish): ")
        if new_product.lower() == "end":
            break
        products.append(new_product)
        print(f"'{new_product}' has been added to the list.")

def delete_product_by_name(products, name):
    if name in products:
        products.remove(name)
        print(f"'{name}' has been removed from the list.")
    else:
        print(f"'{name}' not found in the list.")        

def delete_product(products, index):
    if 0 <= index < len(products):
        deleted_product = products.pop(index)
        print(f"'{deleted_product}' has been removed from the list.")
    else:
        print("\nInvalid index. Product not found.")

def main():
    products = []  # Initialize an empty list for products

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            list_products(products)
        elif choice == "2":
            add_products(products)
        elif choice == "3":
            try:
                index = int(input("Enter the product index to delete: ")) - 1
                delete_product(products, index)
            except ValueError:
                print("\nInvalid input. Please enter a valid index (1, 2, ...).")
        elif choice == "4":
            name_to_delete = input("Enter the product name to delete: ")
            delete_product_by_name(products, name_to_delete)
        elif choice == "5":
            print("\nExiting the program. Thank you!")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-4).")
       
if __name__ == "__main__":
    main()
