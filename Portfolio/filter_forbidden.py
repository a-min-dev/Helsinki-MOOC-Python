"""
The program has a single function, filter_forbidden, which takes two strings as its argument.
The string, forbidden, includes characters that should not be found in the new string that
is to be returned.

The function uses a one-line list comprehension to return a new string in which the forbidden
characters are filtered out.
"""

def filter_forbidden(string: str, forbidden: str):
    return "".join(character for character in string if character not in forbidden)