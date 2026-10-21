'''

Author: Jaeden Souden
Date: January 9, 2026
School: Vectors Institute
Class: Programming Concepts 

A program that allows teachers to:
• Add student records (name, subject, grade)
• View all records
• Search for a student
• Edit or delete student information
• Save and load records from a text file

Criteria: 
- Read/write data to text files correctly; handles file not
found errors

- Uses if/elif/else appropriately for branching decisions

- Implements for and/or while loops meaningfully

- Uses classes to represent core entities (e.g., Student,
Book, Product)

- Presents user with clear choices and input handling

- Proper indentation, variable names, and comments
for clarity

'''
import json


#In session created records are stored here
Records = []

#function that creates a record
def Add_Record():
    
    print("\nInput the following information for the students record. \n")
    
    student_name = input("Name of student: ")
    subject = input("Subject of student: ")
    grade = input("Students grade: ")
    
    Records.append({"Student Name" : student_name, "Subject" : subject, "Grade" : grade})
    
    print("\nRecord Created.")
    
    
#function that presents the user with all loaded or recently recreated records    
def View_All_Records():
    count = 0
    
    if not Records:
        print("No Records Yet.")
        
    else:
        for i, student in enumerate(Records, 0):
            print(f"{i}.Student Name: {Records[i]['Student Name']}\n  Subject: {Records[i]['Subject']}\n  Grade: {Records[i]['Grade']}\n")




#function that searches for a record
def Search():
    name = input("Name of Student who's record to find:  ")
    
    for i, student in enumerate(Records, 0):
        if name == Records[i]['Student Name']:
            print(f"\nStudent Name: {Records[i]['Student Name']}\n  Subject: {Records[i]['Subject']}\n  Grade: {Records[i]['Grade']}")
 
 
    
#function that asks whether the user wants to edit or delete   
def Edit_Delete():
    choice = input("Edit or Delete E/D: ")
    if choice == "E":
        edit()
        
    elif choice == "D":
        delete()
        
        
        
#function to edit a property of a record     
def edit():
    name = input("Name of student who's record info to edit: ")
    info = input("Information to edit (Student Name/Subject/Grade): ")
    change = input("Change to be made: ")
    
    for i, student in enumerate(Records, 0):
        if name == Records[i]['Student Name']:
            Records[i][info] = change
            print(f"\nStudent Name: {Records[i]['Student Name']}\n  Subject: {Records[i]['Subject']}\n  Grade: {Records[i]['Grade']}")


            
#function to delete a record
def delete():
    name = input("Name of student who's record or record info to delete: ")
    
    for i, student in enumerate(Records, 0):
        if name == Records[i]['Student Name']:
            confirm = input("Are you sure? Y/N: ")
            if confirm == "Y":
                del Records[i]
            else:
                break


            
#Function to save current records
def save():
    with open("Records.txt", "a") as f:
        for student_record in Records:
            f.write(str(student_record) + "\n")
            
            
#Function to Load saved records    
def load():
    with open("Records.txt", "r") as f:
        for line in f:
            Records.append(json.loads(line.strip()))
    
    print(Records)
    
    

#Menu System on start-up to interact with Program.
def main():
    
    while True:
        Option = input("""\nOptions:\n
1) Add a students record 
2) View all records 
3) Edit or delete a students information 
4) Search for a students record 
5) Save Current Records 
6) Load Records
7) Exit Program
        \nChoose the corresponding number: """) 

        if Option == "1":
            Add_Record()
        
        elif Option == "2":
            View_All_Records()
            break
        
        elif Option == "3":
            Edit_Delete()
        
        elif Option == "4":
            Search()
            break
        
        elif Option == "5":
            save()
            
        elif Option == "6":
            load()
            
        elif Option == "7":
            break
    
        else:
            print("Not a Valid Option.")
    
    
main()
   
   

#Allows proper viewing of All Records and Searched Record.  
resume = input("Enter 'q' to go back to options  ")

if resume == "q":
    main()
    







