# Write your solution here
# Given 3 different letters, all lowercase or uppercase, find one alphabetically in middle
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

mid_letter = ""
if letter1 < letter2 < letter3 or letter1 > letter2 > letter3:
    mid_letter = letter2
elif letter2 < letter1 < letter3 or letter2 > letter1 > letter3:
    mid_letter = letter1
else:
    mid_letter = letter3

print(f"The letter in the middle is {mid_letter}")