
from typing import List
from Entity.Customer_Task14 import Customer
from Entity.Account_Task14 import Account
class IBankRepository:
    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float) -> Account:
        pass

    def list_accounts(self) -> List[Account]:
        pass

    def calculate_interest(self):
        pass

    def get_account_balance(self, account_number: int) -> float:
        pass

    def deposit(self, account_number: int, amount: float) -> float:
        pass

    def withdraw(self, account_number: int, amount: float) -> float:
        pass

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        pass