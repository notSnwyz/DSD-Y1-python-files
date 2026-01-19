import pandas as pd

df = pd.read_csv("students.csv")

at_risk = df[df["Attendance"] < 80]

df["AtRisk"] = df.index.isin(at_risk.index)

print(df)
print(f"Average Attendance: {df["Attendance"].mean()}")
print(f"Highest Attendance: {df["Attendance"].max()}")
print(f"Lowest Attendance: {df["Attendance"].min()}")
print(f"Number of attendance under 80: {df[df["Attendance"] < 80].shape[0]}")
print(f"Number of attendance over and at 90: {df[df["Attendance"] >= 90].shape[0]}")
print(df["Grade"].value_counts())