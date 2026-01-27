"""
The program creates a student database for a particular course.
Students are added to the database, along with each student's
individual courses and grades.  

The program has multiple functions, including print_student,
which prints the number of courses a particular student has 
completed, the titles of the courses, and the student's average
grade for the completed courses.

Finally, the function, summary, will print out the total number
of students in the database, the name of the student who was 
completed the most courses along with the number of courses completed,
and the name of the student with the best GPA and the corresponding GPA.
"""


def add_student(students: dict, name: str):
    students[name] = {}


def print_student(students: dict, name: str):
    if name not in students: 
        print(f"{name}: no such person in the database")
    else:
        courses = students[name]
        print(f"{name}:")
        
        if len(courses) == 0:
            print(" no completed courses")
        else:
            print(f" {len(courses)} completed courses:")
            total_grade = 0
            # Print each course and grade for the given student
            for course, grade in courses.items():
                print(f"  {course} {grade}")
                total_grade += grade
            # For the given student, find the average grade, or GPA    
            print(f" average grade {total_grade/len(courses)}")    
        

def add_course(students: dict, name: str, course_grade: tuple):
    course, grade = course_grade

    # A course with a grade of 0 shall be ignored when adding course info
    if grade == 0:
        return

    # If a student repeats a course, only the higher grade is recorded
    if course not in students[name] or grade > students[name][course]:
        students[name][course] = grade


def summary(students: dict):
    num_students = len(students)
    max_courses = 0
    max_course_student = ""
    best_grade_avg = 0
    best_grade_avg_student = ""

    for name, courses in students.items():
        if len(courses) > max_courses:
            max_courses = len(courses)
            max_course_student = name

        if len(courses) > 0:
            student_avg = sum(courses.values()) / len(courses)
            if student_avg > best_grade_avg:
                best_grade_avg = student_avg
                best_grade_avg_student = name
    
    print(f"students {len(students)}")
    print(f"most courses completed {max_courses} {max_course_student}")
    print(f"best average grade {best_grade_avg:.1f} {best_grade_avg_student}")


def main():
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)

main()