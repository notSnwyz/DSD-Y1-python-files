import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_sales_dataset.csv")

plt.style.use("dark_background")

def sales_by_category():
    salesByCategory = df.groupby("product_category")["quantity_sold"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(salesByCategory.index, salesByCategory.values)
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.title("Total sales by category")

    plt.tight_layout()
    plt.show()

def sales_by_region():
    salesByRegion = df.groupby("customer_region")["quantity_sold"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(salesByRegion.index, salesByRegion.values)
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.title("Total sales by region")

    plt.tight_layout()
    plt.show()

sales_by_region()