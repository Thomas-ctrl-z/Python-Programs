"""Description: Create a text based Hangman Game
Concepts Used: Loops, Conditionals, String Manipulation
Features to Add: Show the user the guessed letters and the words progress // Add a hint system"""


import random


hangman_wordset = ["welcome", "telescope", "pumpkin", "thunder", "keyboard", "elephant", "volcano", "bracelet",
                    "chocolate", "adventure", "sandwich", "lightning", "butterfly", "mountain", "dinosaur", "treasure"]


mistakes = 0
max_mistakes = 6

# word = random.choice(hangman_wordset)
word = "apple"
word_length = ["_"] * len(word)
guessed = set()



while max_mistakes > mistakes and "_" in word_length:

    print(word_length)
    print("\n")
    user_response = input("Choose a letter: ").strip().lower()

    if len(user_response) != 1 or not user_response.isalpha():
        print("Enter one letter, please \n")
        continue

    if user_response in guessed:
        print("You already guessed that letter \n")
        continue

    guessed.add(user_response)

    
    if user_response in word:
        for i in range(len(word)):
            if word[i] == user_response:
                word_length[i] = user_response

        print("Correct \n")

    else:
        mistakes += 1
        print("Wrong \n")

    if "_" not in word_length:
        print("You win")
    else: 
        print("Game Over")
        print("The word was: ", word)

