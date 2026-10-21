'''

A program for health centre to:
• Add, view, update, or delete clients
• Record client visit and basic stats (blood pressure, heart rate etc) on the visit
• Search for clients
• Save/load the client data from a file

'''

import json


class Client:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class Visit:
    def __init__(self, client_name, date, blood_pressure, heart_rate, temperature):
        self.client_name = client_name
        self.date = date
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.temperature = temperature



clients = []
visits = []


#function Adds Client Information
def Add_Client():
    print("\nEnter Client Information\n")
    name = input("Name: ")
    age = input("Age: ")
    weight = input("Weight (kg): ")
    height = input("Height (cm): ")

    client = Client(name, age, weight, height)
    clients.append(client)
    print("\nClient Added Successfully\n")



#function allows you to view all basic client Information
def View_Clients():
    if not clients:
        print("\nNo Clients Found\n")
    else:
        for c in clients:
            print(f"""
Name: {c.name}
Age: {c.age}
Weight: {c.weight} kg
Height: {c.height} cm
""")

    input("\nPress Enter to return to Main Menu")


#function allows you to update basic client Information
def Update_Client():
    name = input("Client name to update: ")

    for c in clients:
        if c.name == name:
            choice = input("""
What do you want to update?
A) Name
B) Age
C) Weight
D) Height

=====> """).upper()

            value = input("Enter new value: ")

            if choice == "A":
                c.name = value
            elif choice == "B":
                c.age = value
            elif choice == "C":
                c.weight = value
            elif choice == "D":
                c.height = value

            print("Client Updated Successfully")
            return

    print("Client Not Found")

#functoin allows you to delete a clients Information
def Delete_Client():
    name = input("Client name to delete: ")

    for i, c in enumerate(clients):
        if c.name == name:
            confirm = input("Are you sure? (Y/N): ")
            if confirm.upper() == "Y":
                del clients[i]
                print("Client Deleted")
            return

    print("Client Not Found")



#function finds the information for one client
def Search_Client():
    name = input("Client name to search: ")

    for c in clients:
        if c.name == name:
            print(f"""
Name: {c.name}
Age: {c.age}
Weight: {c.weight}
Height: {c.height}
""")
            return

    print("Client Not Found")
    input("\nPress Enter to return to Main Menu")



#function Logs the information from the visit for registered clients
def Record_Visit():
    name = input("Client name: ")

    for c in clients:
        if c.name == name:
            date = input("Visit Date: ")
            bp = input("Blood Pressure: ")
            hr = input("Heart Rate: ")
            temp = input("Temperature: ")

            visit = Visit(name, date, bp, hr, temp)
            visits.append(visit)
            print("Visit Recorded Successfully")
            return

    print("Client Not Found — Add Client First")
    
    
    
    

#function shows all information of clients that visited
def View_Visits():
    if not visits:
        print("\nNo Visits Recorded\n")
    else:
        for v in visits:
            print(f"""
Client: {v.client_name}
Date: {v.date}
Blood Pressure: {v.blood_pressure}
Heart Rate: {v.heart_rate}
Temperature: {v.temperature}
""")

    input("\nPress Enter to return to Main Menu")



#function saves basic information and visit information of client in a txt file
def Save_Data():
    with open("clients.txt", "w") as f:
        for c in clients:
            f.write(json.dumps(c.__dict__) + "\n")

    with open("visits.txt", "w") as f:
        for v in visits:
            f.write(json.dumps(v.__dict__) + "\n")

    print("Data Saved Successfully")



#function loads the visit and basic information of client
def Load_Data():
    clients.clear()
    visits.clear()

    
    with open("clients.txt", "r") as f:
        for line in f:
                data = json.loads(line.strip())
                clients.append(Client(**data))

        with open("visits.txt", "r") as f:
            for line in f:
                data = json.loads(line.strip())
                visits.append(Visit(**data))

        print("Data Loaded Successfully")



def main():
    while True:
        option = input("""
Health Centre System

1) Add Client
2) View Clients
3) Update Client
4) Delete Client
5) Search Client
6) Record Visit
7) View Visits
8) Save Data
9) Load Data
0) Exit

=======> """)

        if option == "1":
            Add_Client()
        elif option == "2":
            View_Clients()
        elif option == "3":
            Update_Client()
        elif option == "4":
            Delete_Client()
        elif option == "5":
            Search_Client()
        elif option == "6":
            Record_Visit()
        elif option == "7":
            View_Visits()
        elif option == "8":
            Save_Data()
        elif option == "9":
            Load_Data()
        elif option == "0":
            break


main()












