
from typing import List
from datetime import datetime

from Entity.Customer_Task14 import Customer
from Entity.Account_Task14 import Account
from Entity.Transaction import Transaction
from Service.IBankRepository import IBankRepository
from Exception.Exception import InsufficientFundException,InvalidAccountException


class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float) -> Account:
        account = Account(acc_no, acc_type, balance, customer)
        self.accounts[acc_no] = account
        return account

    def list_accounts(self) -> List[Account]:
        return list(self.accounts.values())

    def calculate_interest(self):
        pass

    def get_account_balance(self, account_number: int) -> float:
        account = self.accounts.get(account_number)
        if account:
            return account.balance
        else:
            raise InvalidAccountException("Account not found.")

    def deposit(self, account_number: int, amount: float) -> float:
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.transactions.append(Transaction(account, "Deposit", datetime.now(), "Deposit", amount))
            return account.balance
        else:
            raise InvalidAccountException("Account not found.")

    def withdraw(self, account_number: int, amount: float) -> float:
        account = self.accounts.get(account_number)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                self.transactions.append(Transaction(account, "Withdraw", datetime.now(), "Withdraw", amount))
                return account.balance
            else:
                raise InsufficientFundException("Insufficient funds.")
        else:
            raise InvalidAccountException("Account not found.")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):

        pass

    def get_transactions(self, account_number: int, from_date: datetime, to_date: datetime) -> List[Transaction]:

        pass