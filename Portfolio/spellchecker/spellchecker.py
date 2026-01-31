"""
This program asks a user to type in a sentence,
and then the program checks to see if any words are 
misspelled.  

The program checks the words in the sentence
against words found in a provided file.  If a word
is spelled incorrectly by the user, the misspelled
word is placed with two asteriks in an output.
"""

sentence = input("Write text: ")

word_list = set()

with open("wordlist.txt") as word_file:
    for line in word_file:
        word_list.add(line.strip().lower())

result_list = []
sentence_list = sentence.split()
for word in sentence_list:
    if word.lower() not in word_list:
        result_list.append(f"*{word}*")
    else:
        result_list.append(word)

print(" ".join(result_list))



