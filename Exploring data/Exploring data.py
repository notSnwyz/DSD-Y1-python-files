import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set Style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
pd.set_option('display.max_columns', None)

try:
    summer = pd.read_csv("SummerSD.csv")
    winter = pd.read_csv("WinterSD.csv")
    countries = pd.read_csv("CountriesSD.csv")
except FileNotFoundError:
    print("Datasets not found. Please ensure CSV files are in the working directory.")

winter.rename(columns={"Country": "Code"} , inplace=True)
summer["Season"] = "Summer"
winter["Season"] = "Winter"

olympics = pd.concat([summer, winter], ignore_index=True)

olympics_merged = olympics.merge(countries, on="Code", how="left")

olympics_merged["Country"] = olympics_merged["Country_y"].fillna(olympics_merged["Country_x"])
olympics_merged.drop(columns=["Country_x", "Country_y"], inplace=True)

print(f"Combined Data Shape: {olympics_merged.shape}")