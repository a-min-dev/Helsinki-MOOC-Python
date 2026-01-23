"""
The program has a function, all_the_longest, which accepts a list of words
as a paremeter and returns a new list of all the longest words in
the original list.

The function uses for loops to search for the longest-length words in
the list passed to the funciton by comparing the length of each word
with a helper variable.  If a word is found that has a longer length
that the value stored in the helper variable, max_length, then
the list to be returned is initalized with the word as the sole
argument of the list.  Words that have the same length as the
list to be returned are appended to the list;  if a word with a longer
length is found, then the return list is re-initialized. 
"""

def all_the_longest(word_list:list)->list:
    new_list = []
    max_length = 0

    for word in word_list:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            new_list = [word]
    
        elif word_length == max_length:
            new_list.append(word)

    return new_list


def main():
    my_list = ["first", "second", "fourth", "eleventh", "fortieth"]

    result = all_the_longest(my_list)
    print(result)


main()