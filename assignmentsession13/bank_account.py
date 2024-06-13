# bank_account.py

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.accounts = {}  # Dictionary to store account details

    def create_account(self):
        self.account_number = input("Enter account number: ")
        self.account_holder = input("Enter account holder's name: ")

        # Create an account entry in the dictionary
        self.accounts[self.account_number] = {
            "name": self.account_holder,
            "balance": self.balance
        }

        print(f"Account created successfully for {self.account_holder} with account number {self.account_number}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rp {amount}. New balance: Rp {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rp {amount}. New balance: Rp {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        if self.account_number in self.accounts:
            print(f"Account Holder: {self.accounts[self.account_number]['name']}")
            print(f"Account Number: {self.account_number}")
            print(f"Current Balance: Rp {self.balance}")  # Fix this line
        else:
            print("Account not found. Please create an account first.")


# Usage example:
if __name__ == "__main__":
    account = BankAccount()
    account.create_account()
    account.check_balance()
