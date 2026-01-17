# Write your solution here
points = int(input("How many points [0-100]: "))

grade = ""
if points < 0 or points > 100:
   grade = "impossible!"
elif points >= 90:
    grade = 5
elif points >= 80:
    grade = 4
elif points >= 70:
    grade = 3
elif points >= 60:
    grade = 2
elif points >= 50:
    grade = 1
else:
    grade = "fail"

print(f"Grade: {grade}")