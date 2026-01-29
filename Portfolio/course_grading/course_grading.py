"""
This program asks the user for two files:  one file is a CSV
file that includes student IDS and student names, while the
second file is a CSV that includes student IDS and the numnber
of exercises a student has completed each week

The program adds data from each file to a corresponding
dictionary.  Then, the dictionaries are joined with the 
student IDs linking both dictionaries.

Student names and the total number of exercises a student
has completed is printed.
"""

student_prompt = input("Student information: ")
exercises_prompt = input("Exercises completed: ")

students = {}

with open(student_prompt) as student_file:
    for line in student_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

grades = {}

with open(exercises_prompt) as exercises_file:
    for line in exercises_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        grades[parts[0]] = sum(int(exercise) for exercise in parts[1:])

for id, student in students.items():
    if id in grades:
        grade = grades[id]
        print(f"{student} {grade}")
    else:
        print("no student record found")
