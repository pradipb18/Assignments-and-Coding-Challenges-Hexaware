from Customer_Task11 import Customer


class Account:
    lastAccNo = 1001

    def __init__(self, account_type: str, customer: Customer):
        self.AccountNumber = Account.generate_account_number()
        self.AccountType = account_type
        self.AccountBalance = 0.0
        self.Customer = customer

    @staticmethod
    def generate_account_number():
        Account.lastAccNo += 1
        return Account.lastAccNo


class SavingsAccount(Account):
    def __init__(self, account_type="Savings", account_balance=500.0, customer=None, interest_rate=0.0):
        super().__init__(account_type, account_balance, customer)
        self._InterestRate = interest_rate

    @property
    def InterestRate(self):
        return self._InterestRate

    @InterestRate.setter
    def InterestRate(self, interest_rate):
        if isinstance(interest_rate, (float, int)) and interest_rate >= 0:
            self._InterestRate = interest_rate
        else:
            raise ValueError("Interest rate must be a non-negative number.")


class CurrentAccount(Account):
    def __init__(self, account_type="Current", account_balance=0.0, customer=None, overdraft_limit=0.0):
        super().__init__(account_type, account_balance, customer)
        self._OverdraftLimit = overdraft_limit

    @property
    def OverdraftLimit(self):
        return self._OverdraftLimit

    @OverdraftLimit.setter
    def OverdraftLimit(self, overdraft_limit):
        if isinstance(overdraft_limit, (float, int)) and overdraft_limit >= 0:
            self._OverdraftLimit = overdraft_limit
        else:
            raise ValueError("Overdraft limit must be a non-negative number.")


class ZeroBalanceAccount(Account):
    def __init__(self, account_type="ZeroBalance", account_balance=0.0, customer=None):
        super().__init__(account_type, account_balance, customer)