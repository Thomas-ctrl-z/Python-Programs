"""Description: Convert one currency to another using exchange rates.
Concepts Used: User Input, Basic Math
Features to Add: Allow users to choose currency // Fetch real time exchange rates using an API"""

jmd = "jmd"
usd = "usd"

Usd_rate = 155


Base_Currency = input("Base Currency (jmd/usd): ")
Converting_To = input("Currency converting to: ")
Amount = int(input("Amount being converted: "))



if Base_Currency == usd and Converting_To == jmd:
    Answer = Amount * Usd_rate
    print("Your amount in jmd is " + str(Answer))