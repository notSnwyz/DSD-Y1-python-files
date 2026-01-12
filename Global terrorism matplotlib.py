import os
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

path = kagglehub.dataset_download("START-UMD/gtd")

csv_file = [f for f in os.listdir(path) if f.endswith(".csv")][0]
csv_path = os.path.join(path, csv_file)

df = pd.read_csv(csv_path, encoding="ISO-8859-1")

year_counts = df["iyear"].value_counts().sort_index()

plt.style.use("dark_background")

fig, axes = plt.subplots(1, 2, figsize=(18, 6))

axes[0].plot(year_counts.index, year_counts.values, marker="o", linewidth=1)
axes[0].set_title("Number of Terrorist Events per Year")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Number of Events")

axes[0].set_xticks(year_counts.index)
axes[0].tick_params(axis="x", rotation=90)

axes[1].hist(year_counts.values, bins=30)
axes[1].set_title("Distribution of Events per Year")
axes[1].set_xlabel("Events per Year")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()
