#Password Generator
#Add an option to add password to file aka password manager
import random
import copy


letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7"]
symbols = ["!","@","#","$","%","&","*"]

Password_length = int(input("How long do you want your password to be? "))
Include_symbols = input("Should your password include symbols? Y/N: ").upper()
Include_num = input("Should your password include numbers? Y/N: ").upper()
Include_uppercase = input("Should your password include uppercase letters? Y/N: ").upper()

character_pool = letters.copy()

if Include_symbols == "Y":
    character_pool += symbols
    
if Include_num == "Y":
    character_pool += numbers
    
if Include_uppercase == "Y":
    character_pool += [char.upper() for char in letters]

if not character_pool:
    print("Error: No characters to choose from.")
else:
    password_generated = random.choices(character_pool, k=Password_length)
    random.shuffle(password_generated)
    
    corrected_generated_password = ''.join(password_generated)
    print("Generated Password: ", corrected_generated_password)