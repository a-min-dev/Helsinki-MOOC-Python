"""
The program includes a class called LunchCard, which models students at a 
university using a cafeteria meal card.

The constructor for the class takes the initial balance available on the meal
card as its argument.  

The class definition includes several methods, including methods to subtract
from the balance when eating a meal or adding to the balance when depositing money.

If there is not enough money on the meal card to pay for a meal, then the price of the
meal should not be subtracted from the available balance.  Similarly, a student should
not be able to add a negative amount to an existing balance on a meal card.
"""


class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    # Subtract the price of a lunch from the balance if the balance will not go below zero
    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    # Subtract the price of a special from the balance if the balance will not go below zero
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    # Add money to the available balance if the amount is greater than zero
    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Cannot add a negative amount to balance")

        self.balance += amount

# Main function with two students assigned LunchCard objects
peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.deposit_money(20)
graces_card.eat_special()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")