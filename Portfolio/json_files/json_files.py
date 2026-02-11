"""
This program handles a JSON file and prints out information 
about the students in a given course, including the student's name,
age, and hobbies.
"""

import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    # Parse the JSON file to a corresponding Python object (in this scenario, a list of dictionaries)
    persons = json.loads(data)

    # Print information about each person in the above python object
    for person in persons:
        print(f"{person["name"]} {person["age"]} years ({', '.join(person["hobbies"])})")


if __name__ == "__main__":
    result = print_persons("file4.json")