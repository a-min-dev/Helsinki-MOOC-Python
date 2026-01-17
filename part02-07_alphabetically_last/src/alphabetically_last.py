# Write your solution here
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1.lower() < word2.lower():
    print(f"{word2} comes alphabetically last.")
elif word1.lower() > word2.lower():
    print(f"{word1} comes alphabetically last.")
else:
    print(f"You gave the same word twice.")