"""
The program creates a module, string_helper, which contains several functions.

The function change_case swaps lowercase letters for uppercase letters and vice versa.

The split_in_half function splits the parameter string in half and returns the results
in a tuple.  

The remove_special_characters function keeps only alphanumeric characters in the
parameter string.
"""

from string import ascii_letters, digits

def change_case(orig_string: str):
    return orig_string.swapcase()

# Use floor division so that in the case of an odd-length string, the first half is shorter
def split_in_half(orig_string: str):
    mid_point = len(orig_string) // 2
    return (orig_string[:mid_point], orig_string[mid_point:])

def remove_special_characters(orig_string: str):
    # The only allowed characters are alphanumeric characters
    allowed_characters = ascii_letters + digits + ' '
    result = ""

    for char in orig_string:
        if char in allowed_characters:
            result += char

    return result

