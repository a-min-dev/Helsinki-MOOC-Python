# Write your solution here
num = int(input("Please type in a number: "))
if num < 0:
    abs_val = num * -1
else:
    abs_val = num
print(f"The absolute value of this number is {abs_val}")