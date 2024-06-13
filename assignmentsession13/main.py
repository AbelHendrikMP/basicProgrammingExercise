# main.py
from bank_account import BankAccount

def main():
    account = BankAccount()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account.create_account()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: Rp "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: Rp "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "4":
            account.check_balance()
        elif choice == "5":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
