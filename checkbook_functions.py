checkbook = ["500"]

def create_transaction_log(checkbook):
    with open("checkbook_transactions.txt", "a") as f:
        for item in checkbook:
            f.write(item + "\n")

create_transaction_log(checkbook)

def show_transaction_log():
    with open("checkbook_transactions.txt") as f:
        contents = f.readlines()
        for item in contents:
            print(item)

show_transaction_log()



def balance():
    readlines checkbook.txt
    balance = sum all lines
    return balance

def deposit(amount):
    return

def withdraw(amount):
    return



# def make_grocery_list(grocery_list):
#     filename = "my_grocery_list.txt"
#     with open(filename, "a") as f:
#         for item in grocery_list:
#             f.write(item + "\n")

# def get_transaction_log():
#     with open("checkbook_tansactions.txt", 'r') as f:
#         f.readline()

# def cur_balance ():
#     with open(transactions, "r") as f:
#     contents = f.readlines()
#     return sum(contents)
        

# def deposit(amount):
#     transactions(amount)

# def withdraw(amount):
#     transactions(amount)

