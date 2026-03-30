
class InsufficientFundsError(Exception):
    """Exception raised for insufficient funds in a bank account."""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Cannot withdraw more than current balance.") # Raise the custom exception
    return balance - amount

try:
    new_balance = withdraw(100, 50)
    print(f"New balance: {new_balance}")
except InsufficientFundsError as e:
    print(f"Error: {e}") # Output: Error: Cannot withdraw more than current balance.

