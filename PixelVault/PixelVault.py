import pandas as pd

df = pd.read_csv("pixelvault game sales.csv")

print(df.head(5))
print(df.tail(5))

print(df.columns)
print(df.info())

print(df.isna().sum())
print("\n")
print(df.duplicated().any())
print(df[df['total_sale'] != df['price'] * df['quantity']])

print(df["game_title"].value_counts().head(1))
print(df["category"].value_counts().head(1))
print(df["total_sale"].max())
print(df["price"].mean().round(2))