"""
The program asks a user to input a word and a character
to search for in the provided word.  The program finds
all substrings of length 3 that start with the provided 
character.

For example, if the user inputs the word: mississippi with
character: i, the program returns the 
substrings: iss, iss, ipp.
The final i in the word mississippi is not returned, because
the substring has a length less than 3.

An index = -1 shows that the character cannot be found
in the word.
"""


word = input("Please type in a word: ")
character_search = input("Please type in a character: ")
index = word.find(character_search)

while index != -1:

    if len(word) == 0:
        break

    if (len(word) - index) >= 3:
        print(word[index:index+3])
        word = word[index+1:]

        index = word.find(character_search)
    
    # The character may have been found in a shortened
    # substring, but the condition (len(word) - index) >= 3
    # may not be met.  Thus, the loop should break and end
    # the program
    else: 
        break
   