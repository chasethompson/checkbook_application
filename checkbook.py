# Used this resource for json/python https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
import json
from datetime import datetime
# Helpful resource for os.path/pathlib https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
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

    # Run loop for user withdraw option
    elif selection == "2":
        while True:
            withdraw_amount = input("How much cash would you like to withdaw? ")
            if withdraw_amount == "exit":
                cf.exit_program()
            elif withdraw_amount.replace(".", "").isdigit():
                break
            else:
                print(f"{withdraw_amount} is not a valid option. If you want cash, you'll need to enter a numerical value.")
        
        # Enter the correct format
        with = format(float(withdraw_amount), ".2f")
        print(f"Your withdrawn amount is: ${withdraw_amount}")

        # Diplay new balance to user
        new_balance = format((float(balance.read()) - float(withdraw_amount)), ".2f")
        print(f"\nYour current balance is now ${new_balance}")

        # Write over old balance with newly created balance after the withdraw
        balance = (with open("balance.txt", "w"))
        balance.write(str(new_balance))

        # Write entries into the checkbook file
        with open("checkbook.txt", "w") as f:
            json.dump(checkbook, f)

    # Run loop for user deposit option
    elif selection == "3":
        while True:
            deposit_amount = input("How much would you like to deposit today? ")
            if deposit_amount == "exit":
                cf.exit_program()
            elif deposit_amount.replace(".", "").isdigit():
                break
            else:
                print(f"{deposit_amount} is not a valid option. Please enter a numerical value to deposit money.")
        
        # Enter the correct format
        deposit_amount = format(float(deposit_amount), ".2f")
        print(f"Your deposit amount: ${deposit_amount}")

        if deposit_amount == "exit":
            cf.exit_program()

        # Diplay new balance to user
        new_balance = format((float(balance.read()) + float(deposit_amount)), ".2f")
        print(f"\nYour current balance is now ${new_balance}.")

        # Write over old balance with newly created balance after the deposit
        balance = (with open("balance.txt", "w"))
        balance.write(str(new_balance))

        # Write entries into the checkbook file
        with open("checkbook", "w") as f:
            json.dump(checkbook, f)

    # Come back to this, not sure how yet
    elif selection == "4":
        print("New feature coming soon.")
    else:
        cf.exit_program

