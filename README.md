# Helsinki MOOC Python Programming - Python, Data Science + AI Journey
## University of Helsinki 2026

This respository outlines my progress through the University of Helsinki's Python Programming MOOC 2026 from January 2026 to April 2026

## Featured Portfolio
*The following selections demonstrate logical milestones achieved while completing the exercises outlined in the Helsinki MOOC Python & Object Oriented Programming courses:*

* **[classroom_grade_statistics.py](./Portfolio/classroom_grade_statistics.py)** - The program outputs
the grade statistics for a classroom, including the classroom average, the percentage of students who
pass the course, and a histogram of student grades.  The program uses multiple functions to help
calculate the necessary statistics
* **[sudoku_grid.py](./Portfolio/sudoku_grid.py)** - The program checks the validity of a sudoku grid, in which the
numbers 1-9 should appear, at most, once in each row, column,
and 3x3 block within a 9x9 sudoku grid
* **[phone_book.py](./Portfolio/phone_book.py)** - The program prompts the user to select from 3 options:  to search
for a phone number in a phone directory, to add a name and phone number in the phone directory, or quit the program.
The phone directory uses a dictionary with keys representing names and values representing associated phone numbers.
A person is allowed to have multiple phone numbers
* **[student_database.py](./Portfolio/student_database.py)** - The program creates a student base,
which currently stores a student's name and the student's corresponding completed courses and best
grades received in the course.  The summary function prints out statistics which includes which
students has completed the most courses and which student has the best GPA
* **[course_grading.py](./Portfolio/course_grading/course_grading.py)** - The program asks the user for four files:
the first CSV file has student IDS and student names, the second CSV file has student IDs
and the number of exercises a student has completed each week, the third CSV file has
student IDs and the exam scores for each student, and the fourth is a text file with course name and number of credit hours.  Course information and student statistics, including final grades, are written to a .csv file and a .txt file
* **[recipe_search.py](./Portfolio/recipe_search/recipe_search.py)** - The program allows a user to search for recipes
by recipe names, preparation times, or ingredients used in the recipes
* **[city_bikes.py](./Portfolio/city_bikes/city_bikes.py)** - The program uses helper functions to
determine the two city bike stations with the greatest distance between city bike stations in Helsinki, Finland
* **[json_files.py](./Portfolio/json_files/json_files.py)** - The program contains a function which
reads a JSON file, then prints out information about a person, including the person's name, age,
and hobbies
* **[valid_id.py](./Portfolio/valid_id.py)** - The program checks to see if a user's Finnish Personal Identity Code, FPIC, is valid by checking if the birthdate is valid and if a control character is a known valid character
* **[own_language.py](./Portfolio/string_helper/own_language.py)** - The program implements a programming language executor.  The function, run(program), takes a list containing program commands as its argument.  Each item in the list is a line of code in a program.  The function returns a list, which contains results from PRINT commands in the program.  In this scenario, the program will only be passed lines that are in the correct order
* **[shopping_list.py](./Portfolio/shopping_list.py)** - The program includes a ShoppingList class with several methods, such as a method to add an item and the the number of units associated with the item to a shopping list.  The program also includes a function to determine the total number of units in a shopping list
* **[lunchcard_and_paymentterminal.py](./Portfolio/lunchcard_and_paymentterminal.py)** - The program defines two classes, LunchCard and PaymentTerminal.  The LunchCard class definition includes several methods, including one to subtract from the available balance on the lunchard and one to deposit money to the lunchcard.  The PaymentTerminal class definition includes several methods to handle cash and lunchcard payments for meals while keeping track of the total number of meals sold
* **[service_charge.py](./Portfolio/service_charge.py)** - The program defines a class, BankAccount, which models a typical bank account where one can deposit money or withdraw from an available balance.  The class definition includes a private method which charges a 1% fee for each deposit or withdrawal transaction
* **[string_helper.py](./Portfolio/string_helper/string_helper.py)** - The program contains a module, string_helper, which includes several functions, such as one to swap the cases of letters, one to split a string into two parts, and one to remove any special characters from a parameter string
* **[filter_forbidden.py](./Portfolio/filter_forbidden.py)** - The program contains a single function, filter_forbidden, which takes two strings as its arguments:  the string, forbidden, includes characters that should be filtered out of a string that is to be returned by the function.  The function uses a one-line list comprehension statement to return a new string in which forbidden characters are removed
* **[add_numbers_to_list.py](./Portfolio/add_numbers_to_list.py)** - The program defines a function,  which uses recursion, to add numbers to a list until the length of the list is a multiple of 5
* **[course_records.py](./Portfolio/course_records.py)** - The program includes an interactive application where an individual can keep track of individual academic progress, including information on completed courses, the assigned grades, and basic statistics, such as grade point average and total completed credits
* **[ratings.py](./Portfolio/ratings.py)** - The program includes a function, sort_by_ratings, which takes a list of dictionaries, which includes metadata on TV shows, as its argument.  The function sorts the TV shows by ratings using a lambda function
* **[hockey_statistics.py](./Portfolio/hockey_stats/hockey_statistics.py)** - The program includes an application for reviewing NHL statistics (data from 2019-2020 season).  The program works with JSON files, and after the file is provided, the user can examine statistics by selecting an appropriate command, such as searching by player name for individual player stats or searching for n number of players who were the top goal scorers for the entire season
* **[robot_animation.py](./Portfolio/robot_animation/robot_animation.py)** - The program utilizes the pygame module to create an animation of a robot image rounding the perimeter of a window until the user closes the window
* **[robot_invasion.py](./Portfolio/robot_invasion/robot_invasion.py)** - The program utilizes the pygame module to create an animation of random robots falling from the sky (the top of the screen) to the ground (the bottom of the screen).  Once the robots hit the ground, the robots move to the left or to the right until the robot moves off the screen's display


## Tech & Tools
* **Language:** Python 3.x
* **Environment:** VS Code + TMC(Test My Code) Extension
* **Version Control:** Git & GitHub