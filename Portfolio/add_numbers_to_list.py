"""
The program uses recursion to add numbers
to a list until the length of the list is a 
multiple of 5.  The number to be added to
the list is one more than the last item
in the list.
"""

def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        numbers.append(numbers[-1] + 1)
        add_numbers_to_list(numbers)