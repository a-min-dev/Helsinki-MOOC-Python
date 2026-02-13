"""
The program checks to see if a Finnish PIC, 
or Personal Identity Code, is valid.  This can
be similar to checking if a university 
student ID or social security number is valid.

In this scenario, the first 6 digits of one's PIC
represents a birthdate in a ddmmyy format, the
7th character is a century marker, the next 3 
digits are a personal identifier, and the final
character is a control character.

The control character is determined by 
concatenating the 6 digits identifying the 
birthdate and the 3 digits identifying the 
personal indentifier, then dividing by 31.
The control character is found at the index
of a string of digits and characters, where
the index is equal to the remainder when 
dividing the concatenated string by 31.
"""


from datetime import datetime

def is_it_valid(pic: str):
    
    # Each PIC should be 11 characters in length
    if len(pic) != 11:
        return False

    # Birthdate should be in a ddmmyy format
    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])

    # Concatenate the user's birthdate and personal identifier
    user_num_id = int(pic[0:6] + pic[7:10])

    # The string used to determine the control character
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    century_marker = pic[6]

    # Check for a valid century marker
    if century_marker not in "+-A":
        return False

    # Determine the century marker from 1800s - 2000s
    if century_marker == "+":
        full_year = 1800 + year

    elif century_marker == "-":
        full_year = 1900 + year

    elif century_marker == "A":
        full_year = 2000 + year

    else:
        return False

    # Check for a valid date for birthdate
    try:
        test_date = datetime(full_year, month, day)
    except:
        return False

    # Find the control character
    control_character = control_string[user_num_id % 31]

    return control_character == pic[-1]