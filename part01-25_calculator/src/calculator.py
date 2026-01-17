# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operator = input("Operation: ")

if operator == "add":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator == "multiply":
    print(f"{num1} * {num2} = {num1*num2}")
elif operator == "subtract":
    print(f"{num1} - {num2} = {num1-num2}")