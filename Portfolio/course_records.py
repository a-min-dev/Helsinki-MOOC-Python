"""
The following program is an interactive application for a student to
keep track of academic studies.  In the application, a student can
add a course, get course data, and get statistics, such as the total
number of courses completed, the total credits earned, and grade point
average.
"""

# The class, Course, represents a single academic course and corresponding properties
class Course:
    # THe default grade for a course is 0 (ie, the course is not completed)
    def __init__(self, name: str, credits: int):
        self._name = name
        self._credits = credits
        self._grade = 0

    # Getter methods included to allow read-access while keeping privacy
    def name(self):
        return self._name

    def credits(self):
        return self._credits

    def grade(self):
        return self._grade

    # Update the grade if the grade is within the valid range
    def set_grade(self, grade: int):
        if 0 <= grade <= 5:
            self._grade = grade

# The class, StudyTracker, manages the collection of Course objects
class StudyTracker:
    def __init__(self):
        self.__courses = {}

    # Add a new course, or update the number of credits if course exists
    def add_course(self, name: str, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, credits)
        else:
            self.__courses[name]._credits = credits

    # Set a grade if it's higher than the current recorded grade
    def add_grade(self, name: str, grade: int):
        if name in self.__courses:
            # A grade may be raises, but it should never be lowered
            if grade > self.__courses[name].grade():
                self.__courses[name].set_grade(grade)

    # Method to retrieve a Course object by name or return None if course not found
    def get_course(self, name: str):
        return self.__courses.get(name, None)

    # Return the dictionary of all courses for data processing
    def all_courses(self):
        return self.__courses

# The class, StudyApplication, is an interface class which manages input/output
class StudyApplication:
    def __init__(self):
        self.__tracker = StudyTracker()

    # Display a command menu with several options
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    # Calculate and output a summary of statistics and grade distribution
    def stats(self):
        total_credits = 0
        completed_courses = 0
        total_grades = 0

        # Create a frequency table to use for a histogram
        distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

        courses = self.__tracker.all_courses()

        # The courses are sorted alphabetically
        for name in sorted(courses.keys()): 
            course = courses[name] 

            # Iterate through courses that have been completed (assigned a grade)          
            if course.grade() > 0:
                total_credits += course.credits()
                completed_courses += 1
                total_grades += course.grade()
                distribution[course.grade()] += 1
            
        print(f"{completed_courses} completed courses, a total of {total_credits} credits")

        # Statistics, such as grade point average and grade distribution
        if completed_courses > 0:
            mean = total_grades / completed_courses
            print(f"mean {mean:.1f}")
            print("grade distribution")
            for grade in range(5, 0, -1):
                # Grade distribution histogram
                stats = "x" * distribution[grade]
                print(f"{grade}: {stats}")

    # Start of the main application loop
    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("course name: ")
                grade = int(input("grade: "))
                credits = int(input("credits: "))
                self.__tracker.add_course(name, credits)
                self.__tracker.add_grade(name, grade)
            elif command == "2":
                name = input("course name: ")
                course = self.__tracker.get_course(name)

                if course is None:
                    print("no entry for this course")
                # Output for a single searched course
                else:
                    print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")
            elif command == "3":
                self.stats()

# Run the program
if __name__ == "__main__":
    app = StudyApplication()
    app.execute()