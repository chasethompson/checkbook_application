import os
import checkbook_functions as cf

transactions = "checkbook_tranactions.txt"

# Maybe a checkbook initiation function? To create the checkbook log file or see if it exists and use current?

# First line user sees, welcoming them to the checkbook application
greeting = "--- Welcome to your terminal checkbook! ---\n"
print(greeting)

def menu_prompt():
    print("What would you like to do? \n")
    print("1) View your current balance")
    print("2) Make a withdrawal")
    print("3) Make a deposit")
    print("4) Exit")
    selection = input("Your choice? ")
    while selection not in "1234":
        print("Please make a valid selction: " + selection)
        selection = input("What's would you like to do?")
    return selection

menu_prompt()

def menu_option(selection):
    if selection == 1:
        print(f"Your current balance is {cf.balanace}.\n")
        return menu_prompt()
    elif selection == 2:
        amount = input(f"How much would you like to withdraw?\n")
        send amount to cf.withdraw function
    elif selection == 3:
        amount = input(f"How much would you like to deposit?\n")
        send amount to cf.deposit function
    else:
        print(f"Thank you! Have a good day!")


# menu
# valid
# invalid
# balance
# credit
# debit
# exit