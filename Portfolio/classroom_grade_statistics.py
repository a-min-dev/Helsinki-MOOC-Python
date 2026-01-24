"""
This program outputs the grade statistics for a
classroom.  The program includes multiple functions to
determine scores for individual students, such as 
the function exercise_points, which assigns a student
a score based on the number of exercises completed.

The main function asks for the instructor to enter
individual student exam scores and the number of 
exercises completed as a single string per student.
The program continues to ask for student records
until a blank string is entered by the instructor.

The classroom statistics are then printed, including
the percentage of students who passed the course.
A histogram shows the breakdown of the grades for the
classroom.
"""

def exam_exercise_scores(scores: str)->list:
    exam_score, num_exercises = scores.split()
    return [int(exam_score), int(num_exercises)]

def exercise_points(amount: int)->int:
    return amount//10

def grade(points: int)->int:
    grade_cutoffs = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= grade_cutoffs[i]:
            return i

def class_average(points: int)->float:
    return sum(points)/len(points)


def main():
    total_points_list = []
    grades_list = []
    while True:
        student_scores = input("Exam points and exercises completed: ")
        if student_scores == "":
            break
    
        student_record = exam_exercise_scores(student_scores)
        exercise_points_adjusted = exercise_points(student_record[1]) 
        total_score = student_record[0] + exercise_points_adjusted
        total_points_list.append(total_score)
        student_grade = grade(total_score)

        if student_record[0] < 10:
            student_grade = 0
        grades_list.append(student_grade)

    fail_grades = grades_list.count(0)
    pass_grades = len(grades_list) - fail_grades
    pass_percentage = pass_grades/len(grades_list)
    print("Statistics:")
    print(f"Points average: {class_average(total_points_list):.1f}")
    print(f"Pass percentage: {pass_percentage*100:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars_output = "*" * grades_list.count(i)
        print(f"  {i}: {stars_output}")

main()