import matplotlib.pyplot as plt
import kagglehub

# Download latest version
path = kagglehub.dataset_download("START-UMD/gtd")

print("Path to dataset files:", path)

plt.style.use("dark_background")

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Global Terrorism Database")