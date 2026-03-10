import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

def load_data():
    try:
        data = pd.read_csv("Game_Shop_Sales_300_Rows.csv")
        return data
    except:
        print("Error loading file")

def calculate_stats(data):
    avg_units = np.mean(data["Units Sold"])
    total_revenue = np.sum(data["Total Revenue (£)"])

    print("Average Units Sold:", avg_units)
    print("Total Revenue:", total_revenue)

def bar_chart(data):
    category_sales = data.groupby("Category")["Units Sold"].sum()
    category_sales.plot(kind="bar")
    plt.title("Units Sold by Category")
    plt.show()

def line_chart(data):
    data["Date"] = pd.to_datetime(data["Date"])
    sales_by_date = data.groupby("Date")["Units Sold"].sum()
    sales_by_date.plot(kind="line")
    plt.title("Sales Trend Over Time")
    plt.show()

def pie_chart(data):
    category_sales = data.groupby("Category")["Units Sold"].sum()
    category_sales.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Sales Distribution by Category")
    plt.show()

def main():
    data = load_data()
    calculate_stats(data)
    bar_chart(data)
    line_chart(data)
    pie_chart(data)

main()