"""
Description: Count the number of words, characters, or sentences in a text file
Concepts Used: File handling, String Manipulation
"""



def word_count(contents):
    words = contents.split()
    count = len(words)
    print("Number of words in file: ", count)


def char_count(contents):
    count = 0

    for i in contents:
        if i != " ":
            count += 1

    print("Number of characters: ", count)


def sentence_count(contents):
    wordset = contents.split(".")
    count = len(wordset)

    if wordset[-1] == "":
        count -= 1

    print(wordset)
    print("Number of sentences in file: ", count)


with open("demo.txt", "r") as file:
    contents = file.read()
    # contents = contents.replace("\n", "")


user_response = input(" 1. Word Counter \n 2. Character Counter \n 3. Sentence Counter \n -----> ")

if user_response == "1":
    word_count(contents)

elif user_response == "2":
    char_count(contents)

elif user_response == "3":
    sentence_count(contents)

else:
    print("Error.")

