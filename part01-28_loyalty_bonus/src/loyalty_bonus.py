# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points_multiplier = 1.1
    print("Your bonus is 10 %")
else:
    points_multiplier = 1.15
    print("Your bonus is 15 %")

points *= points_multiplier

print(f"You now have {points:.3f} points")