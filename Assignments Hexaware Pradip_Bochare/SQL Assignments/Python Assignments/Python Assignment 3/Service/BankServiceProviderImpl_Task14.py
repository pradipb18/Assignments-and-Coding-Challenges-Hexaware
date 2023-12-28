
from typing import List
from datetime import datetime
from Entity.Customer_Task14 import Customer
from Entity.Account_Task14 import Account
from CustomerServiceProviderImpl_Task14 import CustomerServiceProviderImpl
from IBankServiceProvider_Task14 import IBankServiceProvider
class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        self.account_list = []
        self.transaction_list = []
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer: Customer, acc_type: str, balance: float) -> Account:
        account = Account(acc_type, balance, customer)
        self.account_list.append(account)
        self.accounts_list.append(account)  # Add to the parent class list as well
        return account

    def list_accounts(self) -> List[Account]:
        return self.account_list

    def get_account_details(self, account_number: int):
        for account in self.account_list:
            if account.AccountNumber == account_number:
                return account.get_account_details()
        return None

    def calculate_interest(self):

        pass