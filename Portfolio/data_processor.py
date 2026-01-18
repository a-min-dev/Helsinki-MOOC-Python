"""
This program will ask the user to input
integer numbers. 

When the user inputs 0, that is the signal to finish.

The program should then output the count of
total numbers input (excluding the 0 signaling to end),
the sum of all the numbers, the mean value,
the number of positive integers and the number of
negative integers.

The program uses several counter variables to keep
track of the total number of integers provided by
the user, the running sum of the integers,
the number of positive integers and the number
of negative integers.
"""

print("Please type in integer numbers. Type in 0 to finish.")

count_total = 0
sum_total = 0
count_positive = 0
count_negative = 0

while True:
    num = int(input("Number: "))

    if num == 0:
        break
   
    else:
        count_total += 1
        sum_total += num
        if num > 0:
            count_positive += 1
        else:
            count_negative += 1

if count_total > 0:
    mean = sum_total/count_total

    print(f"Numbers typed in {count_total}")
    print(f"The sum of the numbers is {sum_total}")
    print(f"The mean of the numbers is {mean:.1f}")
    print(f"Positive numbers {count_positive}")
    print(f"Negative numbers {count_negative}")

else:
    print("... exiting with 0 inputs")



