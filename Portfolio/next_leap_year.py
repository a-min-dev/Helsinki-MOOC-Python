"""
A user inputs a year, and the program outputs the next leap year.

A while loop is used to find the next leap year, using the 
condition that the year is a leap year if the year is divible by
4 and if an end-of-century year, such as 2000, that the year
is divisible by 400
"""

year = int(input("Year: "))
next_leap_year = year + 1
while True:
    is_leap_year = False

    if next_leap_year % 4 == 0:
        if next_leap_year % 100 == 0:
            if next_leap_year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        print(f"The next leap year after {year} is {next_leap_year}")
        break     

    next_leap_year += 1





