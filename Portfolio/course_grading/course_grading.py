"""
This program asks the user for three files:  one file is a CSV
file that includes student IDs and student names, the
second file is a CSV that includes student IDs and the numnber
of exercises a student has completed each week, and the third
file is a CSV file that includes student IDs and exam scores.

The program adds data from each file to a corresponding
dictionary.  Then, the dictionaries are joined with the 
student IDs linking the dictionaries.

Student names, exercise points, exam points, total points,
and final grades are printed under a formatted header.
"""

student_prompt = input("Student information: ")
exercises_prompt = input("Exercises completed: ")
exam_prompt = input("Exam points: ")

#File for student names
students = {}
with open(student_prompt) as student_file:
    for line in student_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

#File for exercises completed
exercises = {}
with open(exercises_prompt) as exercises_file:
    for line in exercises_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = sum(int(exercise) for exercise in parts[1:])

#File for exam scores
exams = {}
with open(exam_prompt) as exam_file:
    for line in exam_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0]] = sum(int(exam) for exam in parts[1:])

#Format a header for display student scores and grades
header_name = "name"
header_exec_total = "exec_nbr"
header_exec_points = "exec_pts."
header_exam_points = "exm_pts."
header_tot_points = "tot_pts."
header_grade = "grade"

print(f"{header_name:30}{header_exec_total:10}{header_exec_points:10}{header_exam_points:10}{header_tot_points:10}{header_grade:10}")

for id, student in students.items():
    exercise_score = 0
    grade = 0
    if id in exercises:
        exercise_total = exercises[id]
        exercise_score_cutoffs = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
        for i in range(10, -1, -1):
            if exercise_total >= exercise_score_cutoffs[i]:
                exercise_score = i
                break
    else:
        print("no student record found")

    #Calculate final grades
    if id in exams:
        exam_total = exams[id]
        total_points = exam_total + exercise_score
        grade_cutoffs = [0, 15, 18, 21, 24, 28]
        for j in range(5, -1, -1):
            if total_points >= grade_cutoffs[j]:
                grade = j
                break
    
    #Display statistics for each student that includes exercise scores, exam scores, and final grade           
    print(f"{student:30}{exercise_total:<10}{exercise_score:<10}{exam_total:<10}{total_points:<10}{grade:<10}")



