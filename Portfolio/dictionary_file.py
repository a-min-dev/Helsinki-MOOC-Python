"""
The program acts as a dictionary, in which the user can add
an entry to the dictionary (Finnish word : English word), search by keyword in
the dictionary, or quit the program
"""

import os

file_name = "dictionary.txt"

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_option = int(input("Function: "))

    # Add a dictionary entry
    if user_option == 1:
        finnish_entry = input("The word in Finnish: ")
        english_entry = input("The word in English: ")

        # Write the entry to the .txt file
        with open(file_name, "a") as file:
            file.write(f"{finnish_entry}:{english_entry}\n")
        print("Dictionary entry added")

    # Search by keyword in the dictionary
    elif user_option == 2:
        if os.path.exists(file_name):
            keyword_search = input("Search term: ")
            found = False

            with open(file_name, "r") as file:
                for line in file:
                    parts = line.strip().split(":")
                
                    if len(parts) == 2:
                        finnish_word = parts[0]
                        english_word = parts[1]

                        # The search term maybe be substring of a current dictionary entry
                        if keyword_search in finnish_word or keyword_search in english_word:
                            print(f"{finnish_word} - {english_word}")
                            found = True
            
            if not found:
                print("No matches for the search term were found.")

        else: 
            print("The dictionary is currently empty. Please add an entry first.")

    elif user_option == 3:
        break

print("Bye!")