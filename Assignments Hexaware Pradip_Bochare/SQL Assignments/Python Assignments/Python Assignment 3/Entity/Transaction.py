from datetime import datetime

class Transaction:
    def __init__(self, Account, Description, Transaction_type, Amount):
        self._Account = Account
        self._Description = Description
        self._DateTime = datetime.now()
        self._TransactionType = Transaction_type
        self._TransactionAmount = Amount

    @property
    def Account(self):
        return self._Account

    @property
    def Description(self):
        return self._Description

    @property
    def DateTime(self):
        return self._DateTime

    @property
    def TransactionType(self):
        return self._TransactionType

    @property
    def TransactionAmount(self):
        return self._TransactionAmount

    @TransactionAmount.setter
    def TransactionAmount(self, amount):
        if isinstance(amount, (float, int)) and amount >= 0:
            self._TransactionAmount = amount
        else:
            raise ValueError("Transaction amount must be a non-negative number.")
