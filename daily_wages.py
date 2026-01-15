# Write your solution here
wage_hourly = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")

wage_multiplier = 1
if day == "Sunday":
    wage_multiplier = 2
wage = wage_hourly * hours_worked * wage_multiplier

print(f"Daily wages: {wage} euros") 
