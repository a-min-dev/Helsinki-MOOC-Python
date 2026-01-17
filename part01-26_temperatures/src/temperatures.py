# Write your solution here
temp_fahrenheit = int(input("Please type in a temperature (F): "))

temp_celsius = (temp_fahrenheit - 32) * (5/9)

print(f"{temp_fahrenheit} degrees Fahrenheit equals {temp_celsius} degrees Celsius")
if temp_celsius < 0:
    print("Brr! It's cold in here! ")