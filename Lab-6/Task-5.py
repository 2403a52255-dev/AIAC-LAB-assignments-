# BankAccount class simulates a simple bank account with deposit, withdraw, and balance check functionalities.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Initialize the account with the account holder's name and an optional starting balance (default is 0)
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Deposit a positive amount into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            # If the deposit amount is not positive, show an error message
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        # Withdraw an amount if it is positive and less than or equal to the current balance
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            # If the amount is invalid or insufficient balance, show an error message
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        # Print and return the current balance
        print(f"Current Balance: {self.balance}")
        return self.balance


# --- Check Output ---
# Create a new bank account for 'Namitha' with an initial balance of 500
account1 = BankAccount("Namitha", 500)

# Display the current balance
account1.get_balance()

# Deposit 200 into the account
account1.deposit(200)

# Withdraw 100 from the account
account1.withdraw(100)

# Attempt to withdraw 700, which is more than the current balance; should show an error
account1.withdraw(700)  # Should show insufficient balance

# Display the final balance
account1.get_balance()


