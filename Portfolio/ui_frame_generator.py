"""
The program asks the user the input a string, then
a frame of * characters are printed with the user's
input word placed in the center.

The width of the frame is 30 * characters.

The design handles words that are both even
and odd in length of total characters.
"""



word = input("Word: ")
total_spaces = 28 - len(word)

left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces


print("*" * 30)
print("*" + " " * left_spaces + word + " " * right_spaces + "*")
print("*" * 30)
