from Entity.Customer_Task11 import Customer
from Service.BankServiceProviderImpl_Task11 import BankServiceProviderImpl


class BankApp:
    def __init__(self):
        self.bank_service_provider = BankServiceProviderImpl(branch_name="Main Branch", branch_address="123 Main St")

    def main(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Get Account Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

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
                self.list_accounts()
            elif choice == "8":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


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
        print("3. Zero Balance Account")

        acc_type_choice = input("Enter your choice (1, 2, or 3): ")

        if acc_type_choice == "1":
            acc_type = "Savings"
        elif acc_type_choice == "2":
            acc_type = "Current"
        elif acc_type_choice == "3":
            acc_type = "ZeroBalance"
        else:
            print("Invalid choice. Defaulting to Savings Account.")
            acc_type = "Savings"

        initial_balance = float(input("Enter Initial Balance: "))

        account = self.bank_service_provider.create_account(customer, acc_type, initial_balance)
        if account:
            print(f"Account created successfully. Account Number: {account.AccountNumber}")
        else:
            print("Failed to create account. Please try again.")

    def get_account_balance(self):
        account_number = int(input("Enter Account Number: "))
        balance = self.bank_service_provider.get_account_balance(account_number)
        if balance is not None:
            print(f"Account Balance: {balance}")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        balance = self.bank_service_provider.deposit(account_number, amount)
        print(f"Updated balance: ${balance:.2f}")

    def withdraw(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))
        balance = self.bank_service_provider.withdraw(account_number, amount)
        if balance is not None:
            print(f"Withdrawal successful. Current Balance: {balance:.2f}")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        self.bank_service_provider.transfer(from_account_number, to_account_number, amount)

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        details = self.bank_service_provider.getAccountDetails(account_number)
        if details is not None:
            print(details)

    def list_accounts(self):
        accounts = self.bank_service_provider.listAccounts()
        if accounts:
            print("\nList of Accounts:")
            for account in accounts:
                print(account.get_account_details())
        else:
            print("No accounts found.")


bank_app = BankApp()
bank_app.main()