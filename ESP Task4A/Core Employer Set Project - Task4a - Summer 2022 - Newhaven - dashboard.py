import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Core Employer Set Project - Task4A - Data - Summer 2022 1.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print("1. Return all current data")
    print("2. Return data for a specific region")
    print("3. Return sizes within a selected region")
    print("4. Return region with highest increase in value")
    print("5. Exit")
    return int(input(""))


def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def region_sizes(region):

    if region.lower() in df["Region"].str.lower().values:
        result = df[df["Region"].str.lower() == region.lower()]
        print(result)
        plt.bar(result["Property Type"], result["Rooms"])
        plt.xlabel("Property Type")
        plt.ylabel("Number of rooms")
        plt.title("Number of Rooms by Property Size in " + region.title())
        plt.xticks(rotation = 45)
        plt.tight_layout()
        plt.show()

def highest_value():
    
    df1 = df.loc[:, "Jan-20":"Dec-21"]
    df2 = df.loc[:, "Region Code":"Rooms"]

    result = pd.concat([df2, df1], axis = 1, join = "inner")
    result = pd.DataFrame(result)
    result.dropna(inplace = True)
    result["Increase"] = result["Dec-21"] - result["Jan-20"]
    
    print(result[["Region", "Increase"]])

    plt.bar(result["Region"], result["Increase"])
    plt.xlabel("Region")
    plt.ylabel("Increase in Property Value")
    plt.title("Overall Increase in Property Value by Region")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

while True:
    x = mainmenu()
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")

    elif x == 3:
        region = input("Enter the region you would like to check: ")
        region_sizes(region)
    
    elif x == 4:
        highest_value()

    elif x == 5:
        break

