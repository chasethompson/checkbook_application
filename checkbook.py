import json
from datetime import datetime
import os.path
import checkbook_functions as cf

# Welcome statement for users
print("\n ---- Welcome to your checkbook ---- ")

# Repeats the loop until user exits program
while True: 
    # User selection options
    print("""
Please make a selection:
    1) View Current Balance
    2) Make A Withdraw
    3) Make A Deposit
    4) View Transactions
    6) Exit (You can also type exit at any prompt to Exit )
    """) # Not sure yet if how I'll do 4
    
    # Requires user to enter valid selection
    while True: 
        selection = input("What would you like to do today? ")
        if selection == "exit":
            cf.exit_program()
        elif selection in "1234":
            break
        else:
            print("Invalid entry.")
    # Open current user checkbook file if it exists, if not creates new file
    if os.path.exists("checkbook.txt"): 
        with open("checkbook.txt") as f:
            checkbook = json.load(f)
    else: 
        f= open("checkbook.txt", "w")
        f.write("[]")
        with open("checkbook.txt") as f:
            checkbook = json.load(f)

    # Open current user balance file if it exists, if not creates new file
    if os.path.exists("balance.txt"):
        balance = (open("balance.txt", "r"))
    else: 
        f= open("balance.txt","w")
        f.write("0")
        balance = (open("balance.txt", "r"))
 
    # Print users current balance
    if selection == "1":
        print(f"Your balance is ${balance.read()}.")

    # Run loop for user withdraw options
    elif selection == "2":
        while True: 
