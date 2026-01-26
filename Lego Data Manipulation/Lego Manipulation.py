import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("lego_sets.csv")

#Pie chart for each Theme and how many pieces each set has in each theme.

plt.style.use("dark_background")

themeSets = df.groupby(["theme_name", "set_name"])["piece_count"].sum().reset_index()
themes = themeSets["theme_name"].unique()

cols = 6
rows = math.ceil(len(themes) / cols)

fig, axes = plt.subplots(rows, cols, figsize=(cols*3, rows*3))
axes = axes.flatten()

for i, theme in enumerate(themes):
    data = themeSets[themeSets["theme_name"] == theme]
    axes[i].pie(
        data["piece_count"],
        labels=data["set_name"],
        autopct="%1.1f%%",
        startangle=140,
        textprops={"fontsize": 3}
    )
    axes[i].set_title(theme, fontsize=8)

for j in range(i+1, len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.show()

#Scatter plot with trend line

# plt.style.use("dark_background")
# plt.figure(figsize=(8, 5))
# plt.scatter(df["piece_count"], df["list_price"], None, "#d659ff", alpha=0.3)

# x = df["piece_count"]
# y = df["list_price"]
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)

# plt.plot(x, p(x), "cyan")

# plt.title("Piece Count vs Price")
# plt.xlabel("Piece Count")
# plt.xlabel("Price")
# plt.show()