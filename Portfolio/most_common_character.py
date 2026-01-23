"""
The program uses the function most_common_character with a
string passed as a paremeter to find the character that appears
the most frequently in the string.  In the case of a tie, the
character that appears earliest in the string breaks the tie.

A list of unique letters in the string is initalized to an
empty list.  A set would not work in this case, as a set
is unordered and the order of characters is important
in this program.
"""

def most_common_character(word:str)->str:

    most_common_letter = ""
    max_count = 0
    unique_letters = []
    
    for char in word:
        if char not in unique_letters:
            unique_letters.append(char)
        
    for letter in unique_letters:
        current_count = word.count(letter)
        if current_count > max_count:
            most_common_letter = letter
            max_count = current_count

    return most_common_letter

def main():
    first_string = "aaabbbbbbbccdddddd"
    print(most_common_character(first_string))

main()