'''
Author: Jaeden Souden
Date: January 9, 2026
School: Vectors Institute
Class: Programming Concepts

A program where users can:
• Add books to their personal library (title, author, genre)
• Mark books as read/unread
• Search or delete books
• Persist data using file storage

'''

import json

class library:
    def __init__(self, title, author, genre, mark="Unread"):
        self.title = title
        self.author = author
        self.genre = genre
        self.mark = mark
    
P_Library = []


#function adds the book information to the personal library
def Add_Book():
    print("Input the following information to add your book")
    
    title = input("Title of book: ")
    author = input("Author of book: ")
    genre = input("Genre of the book: ")
    
    book = library(title, author, genre)
    P_Library.append(book)
    
    print("\nBook Added to library\n")


#function finds the requested book information 
def Search_Book():
    title = input("Title of book to find: ")
    
    for i, name in enumerate(P_Library, 0):
        if name.title == title:
            print(f"""\nBook Info:\n
Book Title: {P_Library[i].title}
Book Author: {P_Library[i].author} 
Book Genre: {P_Library[i].genre}
Book Status: {P_Library[i].mark} """)


#function deletes the prompted book
def Delete_Book():
    title = input("Title of book to remove: ")
    
    for i, name in enumerate(P_Library, 0):
        if name.title == title:
            confirm = input("Are you sure? Y/N: ")
            if confirm.upper() == "Y":
                del P_Library[i]
                print("Book Removed")


#function changes the status of prompted book
def Book_Mark():
    title = input("Title of Book's status to change: ")
    status = input("Would You like to set its status to Read or Unread: ")
    
    for i, name in enumerate(P_Library, 0):
        if name.title == title:
            P_Library[i].mark = status
            
            print(f"\nBook Status: {P_Library[i].mark}")
  
    
#function saves the info of the books added in session to a txt file
def Save_Library():
    with open("P_Library.txt", "a") as f:
        for title in P_Library:
            f.write(json.dumps(title.__dict__) + "\n")
    print("library Saved")
    
    
#function loads the info of the books saved from the txt file    
def Load_Library():
    P_Library.clear()
    
    with open("P_Library.txt", "r") as f:
        for line in f:
            data = json.loads(line.strip())
            book = library(**data)
            P_Library.append(book)
    print("library Loaded")

#Main menu where user interacts with the program
def main():

  while True:
      
    Option = input("""
Options:\n
1) Add Book
2) Search for Book
3) Delete Book
4) Mark book as read/unread
5) Save personal library
6) Load library
7) Exit

=======> """)

    if Option == "1":
        Add_Book()
        
    elif Option == "2":
        Search_Book()
        resume = input("\nEnter 'q' to go back to options:  ")
        if resume == "q":
            main()
        break
        
    elif Option == "3":
        Delete_Book()
        
    elif Option == "4":
        Book_Mark()
        
    elif Option == "5":
        Save_Library()
    
    elif Option == "6":
        Load_Library()
        
    elif Option == "7":
        break
      
        
main()






