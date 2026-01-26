"""
The program creates a phone directory that is a dictionary.
In the main function, the user is prompted to select an option
from 3 choices:  1 to search for a phone number, 2 to add
a phone number to the directory, and 3 to quit the program.

The search and add functions are created to either search
for the value associated with a key, or name, or 
add a new key, name, and value, phone number, to the
dictionary.
"""

# The search phone looks for a key, a person's name, in the dictionary
# The function prints "no number" if the key is not found in the dictionary
def search(phone_directory: dict):
    name = input("name: ")
    if name in phone_directory:
        print(phone_directory[name])
    else:   
        print("no number")

# The add function adds a key, a name, and associated value, a phone number
# If the key is already in the dictionary, the phone number is overwritten
def add(phone_directory: dict):
    name = input("name: ")
    phone_number = input("number: ")
    phone_directory[name] = phone_number
    print("ok!")

# The user is prompted to selection from 3 options:  search, add, or quit
def main():
    phone_dict = {}
    while True:
        command_prompt = input("command (1 search, 2 add, 3 quit: )")
        if int(command_prompt) == 1:
            search(phone_dict)
        elif int(command_prompt) == 2:
            add(phone_dict)
        elif int(command_prompt) == 3:
            break
        else:
            print("command is invalid, try again")

    print("quitting...")

main()
