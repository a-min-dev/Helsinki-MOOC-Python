# Write your solution here
num_eat_cafe = int(input("How many times a week do you eat at the student cafeteria? "))
price_lunch = float(input("The price of a typical student lunch? "))
groceries_cost = float(input("How much money do you spend on groceries in a week? "))
weekly_spending = num_eat_cafe * price_lunch + groceries_cost
print("\nAverage food expenditure:")
print(f"Daily: {weekly_spending/7} euros")
print(f"Weekly: {weekly_spending} euros")