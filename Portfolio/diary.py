"""
The program acts as a diary, in which the user can add
an entry to the diary, read any entries in the diary,
or quit the program
"""
import os

file_name = "diary.txt"

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_option = int(input("Function: "))

    if user_option == 1:
        diary_entry = input("Diary entry: ")
        with open(file_name, "a") as file:
            file.write(f"{diary_entry}\n")
        print("Diary saved")

    elif user_option == 2:
        if os.path.exists(file_name):
            print("Entries: ")
            with open(file_name) as file:
                print(file.read().strip())
        else:
            print("no entries in diary")
    
    elif user_option == 0:
        break

print("Bye now!")

