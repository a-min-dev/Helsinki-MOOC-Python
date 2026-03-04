"""
The following program includes the definition for a new class, BankAccount,
which models a typical bank account.  All data attributes within the class
definition are private.

The BankAccount class includes several methods, including the private method,
__service_charge, which decreases the balance of a bank account by 1% 
whenever money is deposited to or withdrawn from an account.  The getter method,
balance, returns the balance of the bank account.
"""

class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    # Ensure the amount to deposit is non-negative
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

        self.__service_charge()

    # Ensure the amount to withdraw is non-negative and there is an available balance
    def withdraw(self, amount: float):
        if self.__balance >= amount and amount > 0:
            self.__balance -= amount

        self.__service_charge()

    # Getter method to return the balance of the bank account
    @property
    def balance(self):
        return self.__balance

    # A private method to apply a 1% fee for any deposit or withdrawal
    def __service_charge(self):
        self.__balance -= self.balance * 0.01


# Test case
account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)