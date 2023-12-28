from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,AccountNumber,CustomerName,Balance):
        self._Accountnumber = AccountNumber
        self._Customername = CustomerName
        self._Balance = Balance

    @property
    def AccountNumber(self):
        return self._AccountNumber

    @AccountNumber.setter
    def AccountNumber(self, new_AccountNumber):
        if isinstance(new_AccountNumber, str) and new_AccountNumber:
            self._AccountNumber = new_AccountNumber
        else:
            raise ValueError("Account number must be a non-empty string.")
    @property
    def CustomerName(self):
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, new_CustomerName):
        if isinstance(new_CustomerName, str) and new_CustomerName:
            self._CustomerName = new_CustomerName
        else:
            raise ValueError("Customer name must be a non-empty string.")
    @property
    def Balance(self):
        return self._Balance


    @Balance.setter
    def Balance(self, new_Balance):
        if isinstance(new_Balance, (int, float)) and new_Balance >= 0:
            self._Balance = new_Balance
        else:
            raise ValueError("Balance must be a non-negative number.")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
class SavingsAccount(BankAccount):
    def __init__(self, account_number="", customer_name="", balance=0.0, interest_rate=0.0):
        super().__init__(account_number, customer_name, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_interest_rate):
        if isinstance(new_interest_rate, (int, float)) and 0 <= new_interest_rate <= 100:
            self._interest_rate = new_interest_rate
        else:
            raise ValueError("Interest rate must be a number between 0 and 100.")

    def deposit(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            self._Balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._Balance:.2f}")
        else:
            raise ValueError("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            if amount <= self._Balance:
                self._Balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self._Balance:.2f}")
            else:
                print("Insufficient balance. Withdrawal failed.")
        else:
            raise ValueError("Withdrawal amount must be a positive number.")

    def calculate_interest(self):
        interest_amount = (self._interest_rate / 100) * self._Balance
        self._Balance += interest_amount
        print(f"Interest calculated and added: ${interest_amount:.2f}. New balance: ${self._Balance:.2f}")

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, account_number="", customer_name="", balance=0.0):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            self._Balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._Balance:.2f}")
        else:
            raise ValueError("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            available_balance = self._Balance + self.OVERDRAFT_LIMIT
            if amount <= available_balance:
                self._Balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self._Balance:.2f}")
            else:
                print("Withdrawal limit exceeded. Withdrawal failed.")
        else:
            raise ValueError("Withdrawal amount must be a positive number.")