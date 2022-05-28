# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count
from posixpath import split
from tracemalloc import stop


def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename,"r")
    return str(file.read())


def count_words():
    text = read_file_content("./story.txt")
    split_text = text.split()
    word_count ={}
    for word in split_text:
        if word in word_count:
            word_count[word] += 1
        else: 
            word_count[word] = 1
    return word_count

print(count_words())


