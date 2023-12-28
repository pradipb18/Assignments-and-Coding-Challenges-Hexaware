from typing import List
from Entity.Customer_Task11 import Customer
from Entity.Account_Task11 import Account
class HMBank:
    def __init__(self):
        self.accounts: List[Account] = []

    def create_account(self, customer, acc_type, balance):
        account = Account(customer, acc_type, balance)
        self.accounts.append(account)
        return account

    def list_accounts(self):
        return sorted(self.accounts, key=lambda acc: acc.Customer.LastName)


bank = HMBank()
account1 = bank.create_account(Customer, "Savings", 1000)
#account2 = bank.create_account(customer2, "Current", 2000)

sorted_accounts = bank.list_accounts()
for account in sorted_accounts:
    print(account.get_account_details())