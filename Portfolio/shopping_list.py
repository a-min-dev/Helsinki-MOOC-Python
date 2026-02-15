"""
The program includes the class ShoppingList, which has
several methods, such as add and amount.

In this scenario, indexing starts from 1, not the
typical 0.

The function, total_units, takes a ShoppingList object
and returns the total units included in the shopping list.
"""

class ShoppingList:
    def __init__(self):
        self.products = []

    # Method to determine the number of items in a shopping list
    def number_of_items(self):
        return len(self.products)

    # Method to add an item to a shopping list, with name and number of units
    def add(self, product: str, number: int):
        self.products.append((product, number))

    # Method to return the nth item in a shopping list (n=1 for first item)
    def item(self, n: int):
        return self.products[n - 1][0]

    # Method to return number of units of nth item (n=1 for first item)
    def amount(self, n: int):
        return self.products[n - 1][1]

# Function to calculate the total number of units in a shopping list
def total_units(my_list: ShoppingList):
    total = 0

    count = my_list.number_of_items()

    # Indexing in this scenario for a ShoppingList object starts at index 1
    for i in range(1, count+1):
        total += my_list.amount(i)
    
    return total


if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))