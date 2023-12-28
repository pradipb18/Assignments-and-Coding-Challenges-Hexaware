from Account import Account
class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type, initial_balance):
        account = Account(account_number, account_type, initial_balance)
        self.accounts.append(account)
        print(f"Account created: {account.AccountType} Account ({account.AccountNumber}) with initial balance ${initial_balance:.2f}")

def main():
    bank = Bank()

    bank.create_account("AC001", "Savings", 1000)

    account1 = bank.accounts[0]
    account1.deposit(500)

    account1.withdraw(200)

    account1.calculate_interest()

if __name__ == "__main__":
    main()