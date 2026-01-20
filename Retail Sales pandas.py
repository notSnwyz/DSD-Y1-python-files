import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("dark_background")

df = pd.read_csv("retail_sales_data.csv")

df["total_sales"] = df["quantity"] * df["price"]

#print(df)

totalRevenue = round(df["price"].sum(), 2)
revenueProduct = df.groupby("product")["total_sales"].sum()
revenueCategory = df.groupby("category")["total_sales"].sum()
top3Products = df.groupby("product")["total_sales"].sum().sort_values(ascending=False).head(3)

revenueProduct.index.name = None
revenueCategory.index.name = None
top3Products.index.name = None

print(totalRevenue)
print(f"Revenue per product: \n{revenueProduct.to_string()}")
print(f"Revenue per category: \n{revenueCategory.to_string()}")
print(f"Top 3 products: \n{top3Products.to_string()}")


def revenue_per_product_bar():
    revenuePerProduct = df.groupby("product")["total_sales"].sum()
    plt.figure(figsize=(10, 6))
    plt.bar(revenuePerProduct.index, revenuePerProduct.values)

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def daily_revenue_line():
    df["revenue"] = df["price"] * df["quantity"]
    dailyRevenue = df.groupby("date")["revenue"].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(dailyRevenue.index, dailyRevenue.values, marker="o")

    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def product_sale_pie():
    productCount = df["product"].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(
        productCount,
        labels=productCount.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Number of Sales by Product Type")
    plt.axis("equal")
    plt.show()

revenue_per_product_bar()
daily_revenue_line()
product_sale_pie()