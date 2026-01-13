# Create a class BankAccount
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Private attributes (using double underscore __)
        self.__owner = owner
        self.__balance = initial_balance

    # Method: get_balance()
    def get_balance(self):
        return self.__balance
    
    # Helper method to get owner (since 'owner' was listed in requirements)
    def get_owner(self):
        return self.__owner

    # Method: deposit(amount)
    def deposit(self, amount):
        # Validation: Deposit must be positive
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive.")

    # Method: withdraw(amount)
    def withdraw(self, amount):
        # Validation: Withdrawal must not exceed balance
        if amount > self.__balance:
            print(f"Error: Insufficient funds. Current balance: ${self.__balance}")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")

# Demonstration of the class functionality
if __name__ == "__main__":
    # Create account
    account = BankAccount("Adilet", 100)
    
    print(f"Account Owner: {account.get_owner()}")
    print(f"Initial Balance: ${account.get_balance()}")
    print("-" * 20)

    # Test Deposit
    account.deposit(50)   # Valid
    account.deposit(-10)  # Invalid (negative)

    print("-" * 20)

    # Test Withdrawal
    account.withdraw(30)  # Valid
    account.withdraw(200) # Invalid (insufficient funds)