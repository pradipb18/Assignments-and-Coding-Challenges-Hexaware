from Customer_Task10 import Customer
class Account:
    account_number_counter = 1001

    def __init__(self, account_type="", account_balance=0.0, customer=None):
        self._AccountNumber = Account.account_number_counter
        Account.account_number_counter += 1
        self._AccountType = account_type
        self._AccountBalance = account_balance
        self._Customer = customer

    @property
    def AccountNumber(self):
        return self._AccountNumber

    @AccountNumber.setter
    def AccountNumber(self, new_account_number):
        if isinstance(new_account_number, str) and new_account_number:
            self._AccountNumber = new_account_number
        else:
            raise ValueError("Account Number must be a non-empty string.")

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, new_account_type):
        if isinstance(new_account_type, str) and new_account_type:
            self._AccountType = new_account_type
        else:
            raise ValueError("Account Type must be a non-empty string.")

    @property
    def AccountBalance(self):
        return self._AccountBalance

    @AccountBalance.setter
    def AccountBalance(self, new_account_balance):
        if isinstance(new_account_balance, (int, float)) and new_account_balance >= 0:
            self._AccountBalance = new_account_balance
        else:
            raise ValueError("Account Balance must be a non-negative number.")

    @property
    def Customer(self):
        return self._Customer

    @Customer.setter
    def Customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._Customer = new_customer
        else:
            raise ValueError("Invalid customer object.")

    def deposit(self, amount):
        if isinstance(amount, (float, int)) and amount > 0:
            self._AccountBalance += amount  # Use the setter here
            print(f"Deposited ${amount:.2f}. New balance: ${self._AccountBalance:.2f}")
            return self._AccountBalance
        else:
            raise ValueError("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.AccountBalance:
            self.AccountBalance -= amount
            return self.AccountBalance
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            return None

    def transfer(self, to_account, amount):
        if amount > 0 and amount <= self.AccountBalance:
            self.AccountBalance -= amount
            to_account.AccountBalance += amount
            print("Transfer successful.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def get_account_details(self):
        return f"Account Number: {self.AccountNumber}, Customer Name: {self.Customer.FirstName} {self.Customer.LastName}, Account Type: {self.AccountType}, Balance: {self.AccountBalance}"