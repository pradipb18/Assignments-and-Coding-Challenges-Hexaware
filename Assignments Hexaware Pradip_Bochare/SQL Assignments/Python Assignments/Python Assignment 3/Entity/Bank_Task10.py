from Customer_Task10 import Customer
from Account_Task10 import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer, acc_type, balance):
        account = Account(customer, acc_type, balance)
        self.accounts[account.AccountNumber] = account
        return account

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].AccountBalance
        else:
            print("Account not found.")
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        else:
            print("Account not found.")
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_account = self.accounts[from_account_number]
            to_account = self.accounts[to_account_number]
            from_account.transfer(to_account, amount)
        else:
            print("One or both accounts not found.")

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_account_details()
        else:
            print("Account not found.")
            return None

'''        
bank = Bank()
customer = Customer("C001", "John", "Doe", "john@example.com", "1234567890", "123 Main St")
account1 = bank.create_account(customer, "Savings", 1000.0)
print(f"Account 1 Number: {account1.AccountNumber}")

account2 = bank.create_account(customer, "Current", 500.0)
print(f"Account 2 Number: {account2.AccountNumber}")
'''

