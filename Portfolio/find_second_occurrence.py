"""
The program asks a user to input a word and a
substring to search for in the provided word.  The program 
finds the second occurrence of the substring in the
user-provided word and outputs the index of the start
of the second occurrence of the substring.

For example, if the user inputs the word: "banana" with
substring: "an", the program returns that the second
occurrence of the substring "an" starts at index = 3

The if statement outside of the while loop handles the
cases where the substring was not found in the word
or the case where the substring was only found once
in the word.
"""

word = input("Please type in a string: ")
substring_search = input("Please type in a substring: ")

index = word.find(substring_search)
count = 0

while index != -1:
    count += 1

    if count == 2:
        print(f"The second occurrence of the substring is at index {index}.")
        break

    index = word.find(substring_search, index + len(substring_search))

if count < 2:
    print("The substring does not occur twice in the string.")