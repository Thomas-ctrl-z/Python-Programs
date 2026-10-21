import random

Random_number = random.randint(1,15)

print("You have five chances to guess the random number")

x = 0
guess = ""

while x < 5:
    guess = int(input("What is your guess? "))

    if guess != Random_number:
        print("Wrong Guess!")
        if guess > Random_number:
            print("You guessed too high, Try Again! \n ")
        elif guess < Random_number:
            print("You guessed too low, Try Again! \n ")

    if guess == Random_number:
            print("You got it Correct \n GG")
            break
    x += 1

print("\n You ran out of guesses")