import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    flag = True

    while flag:
        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("########### Please select an option #############")
        print("### 1. Load and Explore the Data ################")
        print("### 2. Calculate the average number #############")
        print("### 3. Type of post with highest interactions ###")
        print("### 4. Interactions by time of day ##############")
        print("### 5. Matplotlib Visualisations ################")
        print("### 6. Exit #####################################")

        choice = input('Enter your number selection here: ').strip()

        try:
            choice = int(choice)
        except:
            print("Sorry, you did not enter a valid number option")
            flag = True
            continue

        if 1 <= choice <= 6:
            print("Choice accepted!")
            flag = False
        else:
            print("Sorry, you did not enter a valid option")
            flag = True

    return choice


def average_menu():
    flag = True

    while flag:
        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes ##################")
        print("### 2. Average number of Shares #################")
        print("### 3. Average number of Comments ###############")

        choice = input('Enter your number selection here: ').strip()

        try:
            choice = int(choice)
        except:
            print("Sorry, you did not enter a valid number option")
            flag = True
            continue

        if 1 <= choice <= 3:
            print("Choice accepted!")
            flag = False
        else:
            print("Sorry, you did not enter a valid option")
            flag = True

    return choice


def plot_menu():
    flag = True

    while flag:
        print("#################################################")
        print("############## Matplotlib Graphs ################")
        print("#################################################")
        print("########### Please select an option #############")
        print("### 1. Line Chart - Average likes per day #######")
        print("### 2. Bar Chart - Interactions by post type ####")
        print("### 3. Bar Chart - Interactions by time of day ##")

        choice = input('Enter your number selection here: ').strip()

        try:
            choice = int(choice)
        except:
            print("Sorry, you did not enter a valid number option")
            flag = True
            continue

        if 1 <= choice <= 3:
            print("Choice accepted!")
            flag = False
        else:
            print("Sorry, you did not enter a valid option")
            flag = True

    return choice


def convert_avg_men_coice(avg_men_choice):
    
    if avg_men_choice == 1:
        avg_choice = "Likes"
    elif avg_men_choice == 2:
        avg_choice = "Shares"
    else:
        avg_choice = "Comments"  
    
    return avg_choice


def get_avg_data(avg_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    print("Here is the average number of {} each day during the campaign:".format(avg_choice))
    return extract_no_index


def explore_data():
    df = pd.read_csv("Task4a_data.csv")

    print(f"\nThe first 5 rows:")
    print(df.head())

    print("\nThe column names:")
    print(list(df.columns))

    print("\nA short summary of the dataset (info()):")
    df.info()


def add_total_interactions(df):

    if "Total Interactions" not in df.columns:
        df["Total Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
    
    return df

def total_interactions_by_post_type():
    df = pd.read_csv("Task4a_data.csv")
    df = add_total_interactions(df)

    if "Post Type" not in df.columns:
        return "ERROR: Your CSV file must contain a 'Post Type' column for this option."

    totals = df.groupby("Post Type", as_index=False)["Total Interactions"].sum()
    totals = totals.sort_values("Total Interactions", ascending=False)  # FIX

    best = totals.iloc[0]
    print("\nTotal interactions by post type:")
    print(totals.to_string(index=False))
    print("\nBest performing post type overall: {} ({} total interactions)".format(
        best["Post Type"], int(best["Total Interactions"])
    ))

    return ""


def interactions_by_time_of_day():
    df = pd.read_csv("Task4a_data.csv")
    df = add_total_interactions(df)

    if "Time" not in df.columns:
        return "ERROR: Your CSV file must contain a 'Time' column for this option."

    by_time = df.groupby("Time", as_index=False)["Total Interactions"].mean()
    by_time = by_time.sort_values("Total Interactions", ascending=False)

    best = by_time.iloc[0]
    print("\nAverage interactions by time of day:")
    print(by_time.to_string(index=False))
    print("\nTime of day with most interactions: {} (avg {:.2f} interactions)".format(
        best["Time"], float(best["Total Interactions"])
    ))

    return ""


def plot_avg_likes_per_day():
    df = pd.read_csv("Task4a_data.csv")
    avg_likes = df.groupby("Date")["Likes"].mean()

    plt.style.use("dark_background")

    plt.figure()
    plt.plot(avg_likes.index, avg_likes.values)
    plt.title("Average Likes per Day")
    plt.xlabel("Date")
    plt.ylabel("Average Likes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_total_interactions_by_post_type():
    df = pd.read_csv("Task4a_data.csv")
    df = add_total_interactions(df)

    if "Post Type" not in df.columns:
        return "ERROR: Your CSV must contain a 'Post Type' column for this graph."
    
    totals = df.groupby("Post Type", as_index=False)["Total Interactions"].sum()

    plt.style.use("dark_background")

    plt.figure()
    plt.bar(totals["Post Type"], totals["Total Interactions"])
    plt.title("Total Interactions by Post Type")
    plt.xlabel("Post Type")
    plt.ylabel("Total Interactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_interactions_by_time_of_day():
    df = pd.read_csv("Task4a_data.csv")
    df = add_total_interactions(df)

    if "Time" not in df.columns:
        return "ERROR: Your CSV must contain a 'Time' column for this graph."
    
    by_time = df.groupby("Time", as_index=False)["Total Interactions"].mean()

    plt.style.use("dark_background")

    plt.figure()
    plt.bar(by_time["Time"], by_time["Total Interactions"])
    plt.title("Average Interactions by Time of Day")
    plt.xlabel("Time")
    plt.ylabel("Average Interactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


main_menu_choice = main_menu()

if main_menu_choice == 1:
    explore_data()

elif main_menu_choice == 2:
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    print(get_avg_data(avg_choice))

elif main_menu_choice == 3:
    msg = total_interactions_by_post_type()
    if msg:
        print(msg)

elif main_menu_choice == 4:
    msg = interactions_by_time_of_day()
    if msg:
        print(msg)

elif main_menu_choice == 5:
    plot_choice = plot_menu()
    if plot_choice == 1:
        plot_avg_likes_per_day()
    elif plot_choice == 2:
        plot_total_interactions_by_post_type()
    elif plot_choice == 3:
        plot_interactions_by_time_of_day()

else:
    print("Goodbye!")