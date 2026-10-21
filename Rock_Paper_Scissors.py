#Rock Paper Scissors
import random

Computer_choice = ["Rock", "Paper", "Scissors"]

Response = input("Do you think you can beat me in Rock, Paper Scissors? Y/N: ")

if Response == "Y":
    Player_choice = input("Alright. Rock, Paper or Scissors? ").capitalize()
    random.shuffle(Computer_choice)
    print("Shoot! \n" + "Player = " + Player_choice, "\nComputer = " + Computer_choice[0])
elif Response == "N":
    print("Ok, bye bye.")
    exit()
else:
    print("Invalid Input. Enter Y/N ")
    exit()
    
Player_score = 0
Computer_score = 0
    
if Player_choice == Computer_choice[0]:
    print("We're tied! ")
    
elif Player_choice == "Rock" and Computer_choice[0] == "Paper":
    Computer_score += 1
    print("I win! score = " + str(Player_score), "- " + str(Computer_score))
    
elif Player_choice == "Paper" and Computer_choice[0] == "Rock":
    Player_score +=1
    print("You beat me this time.  score = " + str(Player_score), "- " + str(Computer_score))
    
elif Player_choice == "Scissors" and Computer_choice[0] == "Rock":
    Computer_score += 1
    print("I win! score = " + str(Player_score), "- " + str(Computer_score))
    
elif Player_choice == "Rock" and Computer_choice[0] == "Scissors":
    Player_score += 1
    print("You beat me this time. score = " + str(Player_score), "- " + str(Computer_score))
    
elif Player_choice == "Paper" and Computer_choice[0] == "Scissors":
    Computer_score += 1
    print("I win! score = " + str(Player_score), "- " + str(Computer_score))
    
elif Player_choice == "Scissors" and Computer_choice[0] == "Paper":
    Player_score += 1
    print("You beat me this time. score = " + str(Player_score), "- " + str(Computer_score))
    
    
Response_two = input("\n \n Wanna keep trying? Y/N: ").upper()

if Response_two == "Y":
    
    Player_score = 0
    Computer_score = 0
       
    while Response_two == "Y":
        
     Player_choice = input("Alright. Rock, Paper or Scissors? ").capitalize()
     random.shuffle(Computer_choice)
     print("Shoot! \n" + "Player = " + Player_choice, "\nComputer = " + Computer_choice[0])
    
     if Player_choice == Computer_choice[0]:
        print("We're tied! ")
    
     elif Player_choice == "Rock" and Computer_choice[0] == "Paper":
        Computer_score += 1
        print("I win! score = " + str(Player_score), "- " + str(Computer_score))
    
     elif Player_choice == "Paper" and Computer_choice[0] == "Rock":
        Player_score +=1
        print("You beat me this time.  score = " + str(Player_score), "- " + str(Computer_score))
    
     elif Player_choice == "Scissors" and Computer_choice[0] == "Rock":
        Computer_score += 1
        print("I win! score = " + str(Player_score), "- " + str(Computer_score))
    
     elif Player_choice == "Rock" and Computer_choice[0] == "Scissors":
        Player_score += 1
        print("You beat me this time. score = " + str(Player_score), "- " + str(Computer_score))
    
     elif Player_choice == "Paper" and Computer_choice[0] == "Scissors":
        Computer_score += 1
        print("I win! score = " + str(Player_score), "- " + str(Computer_score))
    
     elif Player_choice == "Scissors" and Computer_choice[0] == "Paper":
        Player_score += 1
        print("You beat me this time. score = " + str(Player_score), "- " + str(Computer_score))
    
     Response_two = input("Again? Y/N: ").upper()
     if Response_two == "N":
        print("GG")
        break