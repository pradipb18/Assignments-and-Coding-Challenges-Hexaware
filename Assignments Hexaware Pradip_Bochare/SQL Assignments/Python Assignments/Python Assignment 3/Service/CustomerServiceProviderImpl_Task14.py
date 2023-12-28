from typing import List
from Service.ICustomServiceProvider_Task14 import ICustomerServiceProvider
from datetime import datetime
from Exception.Exception import InvalidAccountException

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts_list = []

    def get_account_balance(self, account_number: int):
        for account in self.accounts_list:
            if account.AccountNumber == account_number:
                return account.AccountBalance
        return None

    def deposit(self, account_number: int, amount: float):
        for account in self.accounts_list:
            if account.AccountNumber == account_number:
                return account.deposit(amount)
        return None

    def withdraw(self, account_number: int, amount: float):
        for account in self.accounts_list:
            if account.AccountNumber == account_number:
                return account.withdraw(amount)
        return None

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        from_account = None
        to_account = None

        for account in self.accounts_list:
            if account.AccountNumber == from_account_number:
                from_account = account
            elif account.AccountNumber == to_account_number:
                to_account = account

        if from_account and to_account:
            from_account.transfer(to_account, amount)
        else:
            raise InvalidAccountException("One or both accounts not found.")

    def get_account_details(self, account_number: int):
        for account in self.accounts_list:
            if account.AccountNumber == account_number:
                return account.get_account_details()
        return None

    def get_transactions(self, account_number: int, from_date: datetime, to_date: datetime):

        pass