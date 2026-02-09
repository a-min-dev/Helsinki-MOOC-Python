"""
The user provides a string that can contain letters, punctuation,
whitespace, or any other characters.

The function imports the string module to separate the user's
string into 3 separate strings:  one which contains only
lowercase and uppercase ascii letters, one which contains only
punctuation, and the third string which contains any other 
characters.
"""

from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    str_letters = ""
    str_punct = ""
    str_etc = ""

    for character in my_string:
        if character in ascii_letters:
            str_letters += character
        elif character in punctuation:
            str_punct += character
        else:
            str_etc += character
    
    return (str_letters, str_punct, str_etc)


if __name__ == "__main__":
    parts = separate_characters("Beyoncé or Taylor Swift? Who do you want to perform at the next Super Bowl?")
    print(parts[0])
    print(parts[1])
    print(parts[2])