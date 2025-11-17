def get_int(x):
    return int(input(x))

def get_float(x):
    return float(input(x))

def get_string(x):
    return str(input(x))

balance = 0.0
money = 0.0
exit = False

while exit == False:
    money = get_float("How much money do you have? ")
    if money > 0.0:
        balance = balance + money
        money = 0.0
        x = get_string("Type exit to stop the program: ")
        if x == "exit" or x == "Exit":
            exit = True
    else:
        print("You have not deposited any money")
        x = get_string("Type exit to stop the program: ")
        if x == "exit" or x == "Exit":
            exit = True

print(f"You currently have {balance} pounds in your balance")