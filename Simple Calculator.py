#Calculator 
#Add advanced operations like exponentiation and/or square roots
#Add A method to switch to a different operator while keeping the current value 
#Add A method to clear the calculator and use a different operator instead of repeating the start button



Operation = input("Addition, Subtraction, Multiplication or Division: ")

def Addition(a,b):
    Answer = (a + b)
    print("The answer is " + str(Answer))
    
    while True:
            number = input("Next number to add(or type 'stop'): ")
            
            if number.lower() == "stop":
                print("Your final answer is " + str(Answer))
                break

                #Declare number as integer after getting its input.
            try:
                number = int(number)
                Answer += number
                print("Your new answer is " + str(Answer))
            except ValueError:
                print("Invalid input. Please enter a number or 'stop'. ")
    return

def Subtraction(a,b):
    Answer = (a - b)
    print('The answer is ' + str(Answer))

    while True:
            number = input("Next number to add(or type 'stop'): ")
            
            if number.lower() == "stop":
                print("Your final answer is " + str(Answer))
                break

            try:
                number = int(number)
                Answer -= number
                print("Your new answer is " + str(Answer))
            except ValueError:
                print("Invalid input. Please enter a number or 'stop'. ")
    return

def Multiplication(a,b):
    Answer = (a * b)
    print('The answer is ' + str(Answer))

    while True:
            number = input("Next number to add(or type 'stop'): ")
            
            if number.lower() == "stop":
                print("Your final answer is " + str(Answer))
                break

            try:
                number = int(number)
                Answer *= number
                print("Your new answer is " + str(Answer))
            except ValueError:
                print("Invalid input. Please enter a number or 'stop'. ")
    return

def Division(a,b):
    Answer = (a / b)
    print('The answer is ' + str(Answer))

    while True:
            number = input("Next number to add(or type 'stop'): ")
            
            if number.lower() == "stop":
                print("Your final answer is " + str(Answer))
                break

            try:
                number = int(number)
                Answer /= number
                print("Your new answer is " + str(Answer))
            except ValueError:
                print("Invalid input. Please enter a number or 'stop'. ")
    return

if Operation == "Addition":
    a = int(input("Enter the first number to Add: "))
    b = int(input("Enter the second number to Add: "))

    Addition(a,b)

if Operation == "Subtraction":
     a = int(input("Enter the first number to Subtract: "))
     b = int(input("Enter the second number to Subtract: "))

     Subtraction(a,b)

if Operation == "Multiplication":
     a = int(input("Enter the first number to Multiply: "))
     b = int(input("Enter the second number to Multiply: "))

     Multiplication(a,b)


if Operation == "Division":
     a = int(input("Enter the first number to be Divided: "))
     b = int(input("Enter the second number to be the Divider: "))

     Division(a,b)