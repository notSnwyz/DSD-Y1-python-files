import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("dark_background")

def main_menu():
    while True:

        print("#################################################")
        print("############## Versere Cars Sales ###############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Total Sales Analysis")
        print("### 2. Trend Analysis (New vs Used)")
        print("### 3. Trend Analysis (Salesperson)")

        choice = input('Enter your number selection here: ').strip()

        if choice in {"1", "2", "3"}:
            return choice
        else:
            print("Invalid choice")


def total_menu ():
    while True:

        print("#################################################")
        print("################# Total Sales ###################")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. All sales by model")   
        print("### 2. Custom selection") 

        choice = input('Enter your number selection here: ').strip()

        if choice in {"1", "2"}:
            return choice
        else:
            print("Invalid choice")


def convert_total_menu_coice(total_menu_choice):
    
    if total_menu_choice == "1":
        total_choice = "All"
    else:
        total_choice = "Model"  
    
    return total_choice

def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data.csv")

    if total_choice == "All":
        extract = df.groupby(['Date','Car Model'], sort=True)['Value'].sum()
        total = df['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    else:
        while True:

            print("########### Please select a model #############")
            print("### 1. Ranger")
            print("### 2. Model D Premium Plus")
            print("### 3. Compass")
            print("### 4. Mercury")
            print("### 5. Outback")
            
            choice = input('Enter your number selection here: ')

            if choice in {"1", "2", "3", "4", "5"}:
                choice = int(choice)
                break
            else:
                print("Invalid choice")

        models = ["Ranger", "Model D Premium Plus", "Compass", "Mercury", "Outback"]   

        custom_choice = models[choice -1]

        extract = df.loc[df['Car Model'] == custom_choice]
        total = extract['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    

    return extract


def trend_menu():
    while True:
        print("#################################################")
        print("############## Trend Analysis ###################")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. New vs Used trend over time")
        print("### 2. Salesperson trend over time")

        choice = input("Enter your number selection here: ")
        if choice in {"1", "2"}:
            return choice
        else:
            print("Invalid choice")


def new_used_trend():
    df = pd.read_csv("Task4a_data.csv")

    group = df.groupby(["Date", "New/Used"])["Value"].sum().reset_index()
    pivot = group.pivot(index="Date", columns="New/Used", values="Value").fillna(0)

    print(df.groupby("New/Used")["Value"].sum().sort_values(ascending=False))

    pivot.sort_index().plot(marker="o")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def salespeople_trend():
    df = pd.read_csv("Task4a_data.csv")

    total = df.groupby("Salesperson")["Value"].sum().sort_values(ascending=False)
    print(total)

    group = df.groupby(["Date", "Salesperson"])["Value"].sum().reset_index()
    pivot = group.pivot(index="Date", columns="Salesperson", values="Value").fillna(0)

    pivot.sort_index().plot(marker="o")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



main_menu_choice = main_menu()

if main_menu_choice == "1":
    total_menu_choice = total_menu()
    total_choice = convert_total_menu_coice(total_menu_choice)
    print(get_total_data(total_choice))
elif main_menu_choice == "2":
    new_used_trend()
elif main_menu_choice == "3":
    salespeople_trend()
