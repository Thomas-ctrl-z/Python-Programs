'''
Author: Jaeden Souden
Date: January 9, 2026
School: Vectors Institute
Class: Programming Concepts

A program for shopkeepers to:
• Add, view, update, or delete product entries
• Record sales by reducing item quantities
• Search inventory
• Save/load the inventory data from a file

'''


import json

class Stock:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    

stock = []    

#function Adds a product entry to the Inventory
def Add_Entry():
    print("\nInput the following information for product entry\n")
    product_name = input("Product Name: ")
    price = input("Product Price: ")
    quantity = input("Product Quantity: ")
    
    product = Stock(product_name, price, quantity)
    stock.append(product)
    print("\nProduct Entry Successfull\n")
    
    
#function allows user to see all product Entries    
def View_Entries():
    if not stock:
        print("No Entries")
        
    else:
        for i, product in enumerate(stock, 0):
            print(f"""Product Name: {stock[i].product_name}
Product Price: {stock[i].price}
Product Quantity: {stock[i].quantity}\n""")
    
    
#function allows user to edit info of any product entry    
def Update_Entry():
    name = input("Product to be updated: ")
    change = input("\nWhat is being changed: \nA)Product Name\nB)Product Price\nC)Product Quantity\n\n======>  ")
    value = input("Input the change your making to the value: ")
    
    for i, product in enumerate(stock, 0):
        if (product.product_name == name and change.upper() == "A"):
            stock[i].product_name = value
            
        elif (product.product_name == name and change.upper() == "B"):
            stock[i].price = value
            
        elif (product.product_name == name and change.upper() == "C"):
            stock[i].quantity == value
            
        print("Change Made Succesfully")    
    
#function allows user to delete a product entry    
def Delete_Entry():
    name = input("Name of product to delete: ")
    
    for i, product in enumerate(stock, 0):
        if product.product_name == name:
            confirm = input("Are you sure? Y/N")
            if confirm.upper() == "Y":
                del stock[i]
                print("Product Deleted")
    
#function tracks sales by reducing product quantity    
def Sales_Tracker():
        name = input("Product name: ")
        amount = input("Amount sold: ")
        
        amount = int(amount)
        
        
        for i, product in enumerate(stock, 0):
            if product.product_name == name:
                
                current_stock = int(stock[i].quantity)
                remaining = current_stock - amount
                remaining = str(remaining)
                
                stock[i].quantity = remaining
                print(f"\nProduct Stock: {stock[i].quantity}\n")
                
    
#function allows user to find the info of a single product    
def Search_Inventory():
    name = input("Name of product to find and display: ")
    
    for i, product in enumerate(stock, 0):
        if product.product_name == name:
            print(f"""\nProduct Name: {stock[i].product_name}
Product Price: {stock[i].price}
Product Quantity: {stock[i].quantity}\n""")
    
  
#function saves all the info of created entries to a txt file    
def Save_Inventory():
    with open("stock.txt", "a") as f:
        for product in stock:
            f.write(json.dumps(product.__dict__) + "\n")
    print("Inventory Saved")
    


#function loads saved txt file of product entries    
def Load_Inventory():
    stock.clear()
    
    with open("stock.txt", "r") as f:
        for line in f:
            data = json.loads(line.strip())
            product = stock(**data)
            stock.append(product)
    print("Inventory Loaded")
    

#Main menu that allows a person to interact with the program.    
def main():
    while True:
        print("Inventory Manager")
        Option = input("""Options:\n
1) Add product entry 
2) View product entry 
3) Update product entry
4) Delete product entry\n
5) Sales Tracker
6) Search Inventory
7) Save inventory data
8) Load inventory data
9) Exit\n
========>  """)

        if Option == "1":
            Add_Entry()
        
        elif Option == "2":
            View_Entries()
            resume = input("\nEnter 'q' to go back to options:  ")
            if resume == "q":
                main()
        
        elif Option == "3":
            Update_Entry()
        
        elif Option == "4":
            Delete_Entry()
        
        elif Option == "5":
            Sales_Tracker()
    
        elif Option == "6":
            Search_Inventory()
            resume = input("\nEnter 'q' to go back to options:  ")
            if resume == "q":
                main()
    
        elif Option == "7":
            Save_Inventory()
        
        elif Option == "8":
            Load_Inventory()
    
        elif Option == "9":
            break

main()

















