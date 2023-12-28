
from Entity.Bank_Task10 import Bank
from Entity.Customer_Task10 import Customer


class BankApp:
    def __init__(self):
        self.bank = Bank()

    def main(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Get Account Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.get_account_balance()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.withdraw()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    def create_account(self):
        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        customer = Customer(customer_id, first_name, last_name, email, phone_number, address)

        print("Choose Account Type:")
        print("1. Savings Account")
        print("2. Current Account")

        acc_type_choice = input("Enter your choice (1 or 2): ")

        if acc_type_choice == "1":
            acc_type = "Savings"
        elif acc_type_choice == "2":
            acc_type = "Current"
        else:
            print("Invalid choice. Defaulting to Savings Account.")
            acc_type = "Savings"

        initial_balance = float(input("Enter Initial Balance: "))

        account = self.bank.create_account(customer, acc_type, initial_balance)
        print(f"Account created successfully. Account Number: {account.AccountNumber}")

    def get_account_balance(self):
        account_number = int(input("Enter Account Number: "))
        balance = self.bank.get_account_balance(account_number)
        if balance is not None:
            print(f"Account Balance: {balance}")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        balance = self.bank.deposit(account_number, amount)
        print(f"Updated balance: ${balance:.2f}")

    def withdraw(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))
        balance = self.bank.withdraw(account_number, amount)
        if balance is not None:
            print(f"Withdrawal successful. Current Balance: {balance:.2f}")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        self.bank.transfer(from_account_number, to_account_number, amount)

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        details = self.bank.get_account_details(account_number)
        if details is not None:
            print(details)

bank_app = BankApp()
bank_app.main()