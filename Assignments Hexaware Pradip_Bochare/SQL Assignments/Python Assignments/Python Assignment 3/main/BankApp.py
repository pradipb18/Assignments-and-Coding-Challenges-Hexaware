from Service.CustomerServiceProviderImpl_Task14 import CustomerServiceProviderImpl
from datetime import datetime
from Service.BankServiceProviderImpl_Task14 import BankServiceProviderImpl
from Entity.Customer_Task14 import Customer
from Exception.Exception import InvalidAccountException,InsufficientFundException,OverDraftLimitExceededException
class BankApp:
    def __init__(self):

        self.customer_service_provider = CustomerServiceProviderImpl()
        self.bank_service_provider = BankServiceProviderImpl()

    def main(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                self.list_accounts()
            elif choice == "8":
                self.get_transactions()
            elif choice == "9":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

    def create_account(self):
        while True:
            print("\nChoose Account Type:")
            print("1. Savings Account")
            print("2. Current Account")
            print("3. Zero Balance Account")
            print("4. Back to Main Menu")

            acc_type_choice = input("Enter your choice (1-4): ")

            if acc_type_choice == "1":
                self.create_savings_account()
            elif acc_type_choice == "2":
                self.create_current_account()
            elif acc_type_choice == "3":
                self.create_zero_balance_account()
            elif acc_type_choice == "4":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def create_savings_account(self):
        customer = self.get_customer_details()
        acc_no = self.generate_account_number()
        acc_type = "Savings"
        balance = float(input("Enter Initial Balance: "))
        self.bank_service_provider.create_account(customer, acc_no, acc_type, balance)
        print(f"Savings Account created successfully. Account Number: {acc_no}")

    def create_current_account(self):
        customer = self.get_customer_details()
        acc_no = self.generate_account_number()
        acc_type = "Current"
        balance = float(input("Enter Initial Balance: "))
        self.bank_service_provider.create_account(customer, acc_no, acc_type, balance)
        print(f"Current Account created successfully. Account Number: {acc_no}")

    def create_zero_balance_account(self):
        customer = self.get_customer_details()
        acc_no = self.generate_account_number()
        acc_type = "Zero Balance"
        balance = 0.0
        self.bank_service_provider.create_account(customer, acc_no, acc_type, balance)
        print(f"Zero Balance Account created successfully. Account Number: {acc_no}")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        new_balance = self.bank_service_provider.deposit(account_number, amount)
        print(f"Deposit successful. New Balance: {new_balance:.2f}")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        try:
            new_balance = self.bank_service_provider.withdraw(account_number, amount)
            print(f"Withdrawal successful. New Balance: {new_balance:.2f}")
        except InsufficientFundException as e:
            print(f"Error: {e}")

    def get_balance(self):
        account_number = int(input("Enter account number: "))
        try:
            balance = self.bank_service_provider.get_account_balance(account_number)
            print(f"Account Balance: {balance:.2f}")
        except InvalidAccountException as e:
            print(f"Error: {e}")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        try:
            self.bank_service_provider.transfer(from_account_number, to_account_number, amount)
            print("Transfer successful.")
        except (InvalidAccountException, InsufficientFundException) as e:
            print(f"Error: {e}")

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        try:
            details = self.bank_service_provider.get_account_details(account_number)
            print(details)
        except InvalidAccountException as e:
            print(f"Error: {e}")

    def list_accounts(self):
        accounts = self.bank_service_provider.list_accounts()
        if accounts:
            print("\nList of Accounts:")
            for account in accounts:
                print(account)
        else:
            print("No accounts found.")

    def get_transactions(self):
        account_number = int(input("Enter Account Number: "))
        from_date = datetime.strptime(input("Enter From Date (YYYY-MM-DD): "), "%Y-%m-%d")
        to_date = datetime.strptime(input("Enter To Date (YYYY-MM-DD): "), "%Y-%m-%d")
        try:
            transactions = self.bank_service_provider.get_transactions(account_number, from_date, to_date)
            if transactions:
                print("\nList of Transactions:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found.")
        except InvalidAccountException as e:
            print(f"Error: {e}")

    def generate_account_number(self):
        return 1234567890

    def get_customer_details(self):

        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        return Customer(customer_id, first_name, last_name, email, phone_number, address)


bank_app = BankApp()

bank_app.main()