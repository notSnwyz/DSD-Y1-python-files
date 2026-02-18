import pandas as pd
import matplotlib.pyplot as plt

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show an item sales over time")
        print("3. Item sales at lunch versus dinner over time")
        print("4. Highest total sales and average sales within a time period")

        main_menu_choice = input("Please enter the number of your choice (1-4): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 4:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

def plot_items_over_time(item, startdate, enddate):

    plt.style.use("dark_background")

    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    plt.plot(df3.columns, df3.values[0])
    plt.title("Sales of {} between {} and {}.".format(item, startdate, enddate))
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()

def plot_lunch_versus_dinner(item, startdate, enddate):

    plt.style.use("dark_background")

    df1 = pd.read_csv("Task4a_data.csv") 
    lunchItem = df1.loc[df1["Service"] == "Lunch"]
    lunchDf = lunchItem.loc[:,startdate:enddate]
    dinnerItem = df1.loc[df1["Service"] == "Dinner"]
    dinnerDf = dinnerItem.loc[:,startdate:enddate]

    plt.plot(lunchDf.columns, lunchDf.values[0], label = "Lunch")
    plt.plot(dinnerDf.columns, dinnerDf.values[0], label = "Dinner")
    plt.legend()
    plt.title("Sale of {} at lunch versus dinner between {} and {}".format(item, startdate, enddate))
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()

def total_average_sales(startdate, enddate): #WIP

    df1 = pd.read_csv("Task4a_data.csv")
    items = df1.loc[df1["Menu Item"]]
    dates = items.loc[:, startdate:enddate]

    print(dates)

main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)

elif main_menu == 2:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_start_date()

    plot_items_over_time(item, start_date, end_date)

elif main_menu == 3:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_start_date()

    plot_lunch_versus_dinner(item, start_date, end_date)

elif main_menu == 4:

    start_date = get_start_date()
    end_date = get_start_date()

    total_average_sales(start_date, end_date)