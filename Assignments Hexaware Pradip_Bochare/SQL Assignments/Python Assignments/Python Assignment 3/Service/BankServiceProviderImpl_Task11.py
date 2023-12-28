

from IBankServiceProvider_Task11 import IBankServiceProvider
from CustomerServiceProviderImpl_Task11 import CustomerServiceProviderImpl


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.accountList = []
        self.branchName = branch_name
        self.branchAddress = branch_address

    def create_account(self, customer, acc_type, balance):
        account = super().create_account(customer, acc_type, balance)
        self.accountList.append(account)
        return account

    def list_accounts(self):
        return self.accountList

    def calculate_interest(self):
        for account in self.accountList:
            pass