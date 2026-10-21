#Simulate rolling dice with random results
#Concepts: Random numbers, loops
"""Features to Add: Support multiple dice and different dice types(eg d6, d10)
Add a feature to calculate the total roll value"""

import random 

sides = ""
total_roll = 0

while True:
    sides = int(input("\nHow many sides? "))
    
    if sides < 1 :
        break
    
    dice_amount = int(input("How many dice? "))
    
    if dice_amount > 1:
        for x in range(dice_amount ):
            roll = random.randint(1,sides)
            print(f"\nroll = {roll}")
            total_roll = total_roll + roll
            print(f"Total roll value = {total_roll}")
    else:
        roll = random.randint(1,sides)
        total_roll = total_roll + roll
        print(f"\nroll = {roll}")
        print(f"Total roll value = {total_roll}")
    
    
print("\no7")