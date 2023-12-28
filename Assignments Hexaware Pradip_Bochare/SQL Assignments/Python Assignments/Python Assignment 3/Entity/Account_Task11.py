from Customer_Task11 import Customer
class Account:
    lastAccNo = 1001

    def __init__(self, account_type="", account_balance=0.0, customer=None):
        self._AccountNumber = Account.generate_account_number()
        self._AccountType = account_type
        self._AccountBalance = account_balance
        self._Customer = customer

    @property
    def AccountNumber(self):
        return self._AccountNumber

    @property
    def AccountType(self):
        return self._AccountType

    @property
    def AccountBalance(self):
        return self._AccountBalance

    @property
    def Customer(self):
        return self._Customer

    def deposit(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            self._AccountBalance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._AccountBalance:.2f}")
            return self._AccountBalance
        else:
            raise ValueError("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.AccountBalance:
            self._AccountBalance -= amount
            return self._AccountBalance
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            return None


    @staticmethod
    def generate_account_number():
        Account.lastAccNo += 1
        return Account.lastAccNo

class SavingsAccount(Account):
    def __init__(self, account_balance=500.0, interest_rate=0.02, customer=None):
        super().__init__("Savings", account_balance, customer)
        self._InterestRate = interest_rate
    @property
    def InterestRate(self):
        return self._InterestRate

class CurrentAccount(Account):
    def __init__(self, account_balance=0.0, overdraft_limit=1000.0, customer=None):
        super().__init__("Current", account_balance, customer)
        self._OverdraftLimit = overdraft_limit
    @property
    def OverdraftLimit(self):
        return self._OverdraftLimit
    def withdraw(self, amount):
        total_withdrawal = amount + abs(min(0, self.AccountBalance))
        if total_withdrawal <= (self.AccountBalance + self.OverdraftLimit):
            self._AccountBalance -= amount
            print(f"Withdrawn ${amount:.2f}. New balance: ${self._AccountBalance:.2f}")
            return self._AccountBalance
        else:
            print("Invalid withdrawal amount or exceeding overdraft limit.")
            return None

class ZeroBalanceAccount(Account):
    def __init__(self, customer=None):
        super().__init__("ZeroBalance", 0.0, customer)