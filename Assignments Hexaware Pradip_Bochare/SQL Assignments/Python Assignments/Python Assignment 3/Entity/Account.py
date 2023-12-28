class Account:
    def __init__(self, AccountNumber, AccountType, AccountBalance):
        self._AccountNumber = AccountNumber
        self._AccountType = AccountType
        self._AccountBalance = AccountBalance

    @property
    def AccountNumber(self):
        return self._AccountNumber

    @AccountNumber.setter
    def AccountNumber(self, new_AccountNumber):
        if isinstance(new_AccountNumber, str) and new_AccountNumber:
            self._AccountNumber = new_AccountNumber
        else:
            raise ValueError("Account Number must be a non-empty string.")

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, new_AccountType):
        if isinstance(new_AccountType, str) and new_AccountType:
            self._AccountType = new_AccountType
        else:
            raise ValueError("Account Type must be a non-empty string.")

    @property
    def AccountBalance(self):
        return self._AccountBalance

    @AccountBalance.setter
    def AccountBalance(self, new_AccountBalance):
        if isinstance(new_AccountBalance, (int, float)) and new_AccountBalance >= 0:
            self._AccountBalance = new_AccountBalance
        else:
            raise ValueError("Account Balance must be a non-negative number.")

    def deposit(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            self._AccountBalance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._AccountBalance:.2f}")
        else:
            raise ValueError("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            if amount <= self._AccountBalance:
                self._AccountBalance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self._AccountBalance:.2f}")
            else:
                print("Insufficient balance. Withdrawal failed.")
        else:
            raise ValueError("Withdrawal amount must be a positive number.")

    def calculate_interest(self):
        interest_rate = 4.5
        interest_amount = (interest_rate / 100) * self._AccountBalance
        print(f"Interest calculated: ${interest_amount:.2f}")
        return interest_amount

class SavingsAccount(Account):
    def __init__(self, account_number, account_balance, interest_rate):
        super().__init__(account_number, "Savings",account_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = (self.interest_rate / 100) * self._AccountBalance
        self._AccountBalance += interest_amount
        print(f"Interest calculated and added: ${interest_amount:.2f}. New balance: ${self._AccountBalance:.2f}")

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000
    def __init__(self, account_number, account_balance):
        super().__init__(account_number, "Current",account_balance)
    def withdraw(self, amount):
        if amount > 0:
            available_balance = self._AccountBalance + self.OVERDRAFT_LIMIT
            if amount <= available_balance:
                self._AccountBalance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self._AccountBalance:.2f}")
            else:
                print("Withdrawal limit exceeded. Withdrawal failed.")
        else:
            raise ValueError("Withdrawal amount must be greater than 0.")