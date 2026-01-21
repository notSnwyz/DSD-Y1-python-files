import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve by type")
        print("### 3. Issues based on region")
        print("### 4. Resolution based on region")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########### Please select an issue type ############")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

# Submenu for time taken to resolve, provides type check validation for the input and returns issue type as a string

def resolve_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Resolve time by type ################")
        print("####################################################")
        print("")
        print("########### Please select an issue type ############")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then gets the mean of the days taken to resolve of the requested issue type

def get_resolve_data(resolve_menu_choice):
    issues = pd.read_csv("Task4a_data.csv")

    times = issues.groupby("Issue Type")["Days To Resolve"].mean()
    time = times[resolve_menu_choice]

    msg = "The mean time taken to resolve the issue logged as a {} was: {:.2f} days.".format(resolve_menu_choice, time)
    return msg

def issue_bar():
    plt.style.use("dark_background")
    issues = pd.read_csv("Task4a_data.csv")

    counts = (
        issues
        .groupby(["Region", "Issue Type"])
        .size()
        .reset_index(name="Count")
    )

    pivot = counts.pivot(
        index="Region",
        columns="Issue Type",
        values="Count"
    ).fillna(0)

    pivot.plot(
        kind="bar",
        figsize=(9,5),
        width=0.8
    )
    
    plt.xlabel("Region")
    plt.ylabel("Number of Issues")
    plt.title("Issue Counts by Region and Type")
    plt.legend(title="Issue Type")
    plt.tight_layout()
    plt.show()

    

main_menu_choice = main_menu()
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))
elif main_menu_choice == "2":
    resolve_menu_choice = resolve_menu()
    print(get_resolve_data(resolve_menu_choice))
elif main_menu_choice == "3":
    issue_bar()
