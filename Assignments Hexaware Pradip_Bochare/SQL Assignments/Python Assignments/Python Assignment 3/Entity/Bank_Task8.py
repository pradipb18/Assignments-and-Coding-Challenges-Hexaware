from Account import Account,SavingsAccount,CurrentAccount
class Bank:
    def create_account(self):
        print("Select account type:")
        print("1. Savings Account")
        print("2. Current Account")
        choice = int(input("Enter your choice (1 or 2): "))
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))

        if choice == 1:
            interest_rate = float(input("Enter interest rate for savings account: "))
            return SavingsAccount(account_number, initial_balance, interest_rate)
        elif choice == 2:
            return CurrentAccount(account_number, initial_balance)
        else:
            print("Invalid choice. Creating a generic account.")
            return Account(account_number, "Generic", initial_balance)

    def main(self):
        print("Customer Create Acccount first follow below steps")
        account = self.create_account()

        while True:
            print("\nSelect operation:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest (for Savings Account)")
            print("4. Exit")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == 3:
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print("Interest calculation not applicable for the current account.")
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

bank = Bank()
bank.main()