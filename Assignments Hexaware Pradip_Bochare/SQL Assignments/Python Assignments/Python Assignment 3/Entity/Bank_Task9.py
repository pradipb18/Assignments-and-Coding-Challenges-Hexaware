from BankAccount_Task9 import SavingsAccount,CurrentAccount
class Bank:
    def main(self):
        while True:
            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Exit")

            choice = input("Enter your choice (1, 2, or 3): ")

            if choice == '1':
                account_type = "Savings"
            elif choice == '2':
                account_type = "Current"
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

            account = self.create_account(account_type)
            self.perform_operations(account)

    def create_account(self, account_type):
        account_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))

        if account_type == "Savings":
            interest_rate = float(input("Enter interest rate for savings account: "))
            return SavingsAccount(account_number, customer_name, initial_balance, interest_rate)
        elif account_type == "Current":
            return CurrentAccount(account_number, customer_name, initial_balance)
        else:
            print("Invalid account type.")
            return None

    def perform_operations(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest (for Savings Account)")
            print("4. Exit")

            choice = input("Enter your choice (1, 2, 3, or 4): ")

            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3' and isinstance(account, SavingsAccount):
                account.calculate_interest()
            elif choice == '4':
                print("Exiting account operations.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                continue

bank = Bank()
bank.main()