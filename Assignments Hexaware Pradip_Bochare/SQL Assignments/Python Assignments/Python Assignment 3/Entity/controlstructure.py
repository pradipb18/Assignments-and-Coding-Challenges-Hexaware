#TASK 1
def check_loan_eligibility(credit_score, annual_income):
    if credit_score > 700 and annual_income >= 50000:
        return True
    else:
        return False
def main():

    credit_score = int(input("Enter your credit score: "))
    annual_income = float(input("Enter your annual income: $"))

    eligibility = check_loan_eligibility(credit_score, annual_income)

    if eligibility:
        print("Congratulations! You are eligible for a loan.")
    else:
        print("Sorry, you are not eligible for a loan at this time.")

#TASK2
def check_balance(balance):
    print(f"Your current balance: ${balance}")

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds. Withdrawal failed.")
    elif amount % 100 != 0 or amount <= 0:
        print("Invalid withdrawal amount. Please enter a multiple of 100 and greater than 0.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ${balance}")
    return balance

def deposit(balance, amount):
    if amount <= 0:
        print("Invalid deposit amount. Please enter an amount greater than 0.")
    else:
        balance += amount
        print(f"Deposit successful. New balance: ${balance}")
    return balance

def main1():

    current_balance = float(input("Enter your current balance: $"))

    print("\nATM Options:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    # Get user choice
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        check_balance(current_balance)
    elif choice == 2:
        withdrawal_amount = float(input("Enter the amount to withdraw: $"))
        current_balance = withdraw(current_balance, withdrawal_amount)
    elif choice == 3:
        deposit_amount = float(input("Enter the amount to deposit: $"))
        current_balance = deposit(current_balance, deposit_amount)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

#TASK 3
def calculate_future_balance(initial_balance, annual_interest_rate, years):
    future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
    return future_balance


def main2():
    num_customers = int(input("Enter the number of customers: "))

    for customer in range(1, num_customers + 1):
        print(f"\nCustomer {customer}:")

        initial_balance = float(input("Enter the initial balance: $"))
        annual_interest_rate = float(input("Enter the annual interest rate (%): "))
        years = int(input("Enter the number of years: "))

        future_balance = calculate_future_balance(initial_balance, annual_interest_rate, years)

        print(f"Future Balance for Customer {customer}: ${future_balance:.2f}")

#TASK 4
def get_account_balance(accounts, account_number):
    if account_number in accounts:
        return accounts[account_number]
    else:
        return None
def main3():
    bank_accounts = {
        "123456": 1000.50,
        "789012": 500.25,
        "345678": 1500.75
    }
    while True:

        account_number = input("Enter your account number: ")

        account_balance = get_account_balance(bank_accounts, account_number)

        if account_balance is not None:
            print(f"Account Balance for Account {account_number}: ${account_balance:.2f}")
            break
        else:
            print("Invalid account number. Please try again.")

#TASK 5
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True


def main4():
    password = input("Create your bank account password: ")

    if is_valid_password(password):
        print("Password is valid. Account created successfully!")
    else:
        print("Invalid password. Please make sure your password meets the specified criteria.")

#TASK 6
def display_transaction_history(transaction_history):
    print("\nTransaction History:")
    for transaction in transaction_history:
        print(transaction)
def main5():
    transaction_history = []
    while True:
        print("\nOptions:")
        print("1. Add Deposit")
        print("2. Add Withdrawal")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            deposit_amount = float(input("Enter the deposit amount: $"))
            transaction_history.append(f"Deposit: +${deposit_amount:.2f}")
        elif choice == '2':
            withdrawal_amount = float(input("Enter the withdrawal amount: $"))
            transaction_history.append(f"Withdrawal: -${withdrawal_amount:.2f}")
        elif choice == '3':
            display_transaction_history(transaction_history)
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")




if __name__ == "__main__":
   main() #TASK 1

if __name__ == "__main__":
   main1() #TASK 2

if __name__ == "__main__":
   main2() #TASK 3
if __name__ == "__main__":
   main3() #TASK 4
if __name__ == "__main__":
    main4()  # TASK 5

if __name__ == "__main__":
    main5()  # TASK 6
