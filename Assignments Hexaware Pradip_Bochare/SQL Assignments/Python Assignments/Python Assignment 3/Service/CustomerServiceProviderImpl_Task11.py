from Service.ICustomerServiceProvider_Task11 import ICustomerServiceProvider
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = []

    def get_account_balance(self, account_number):
        for account in self.accounts:
            if account.AccountNumber == account_number:
                return account.AccountBalance
        return None

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.AccountNumber == account_number:
                return account.deposit(amount)
        return None

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.AccountNumber == account_number:
                return account.withdraw(amount)
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        to_account = None

        for account in self.accounts:
            if account.AccountNumber == from_account_number:
                from_account = account
            elif account.AccountNumber == to_account_number:
                to_account = account

        if from_account and to_account:
            from_account.transfer(to_account, amount)
        else:
            print("One or both accounts not found.")

    def get_account_details(self, account_number):
        for account in self.accounts:
            if account.AccountNumber == account_number:
                return account.get_account_details()
        return None