# main.py
from calculartor_modules import *

def main():
    while True:
        print("Welcome to the Simple Calculator!")
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
