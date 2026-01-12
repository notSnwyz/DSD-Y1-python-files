import matplotlib.pyplot as plt

plt.style.use("dark_background")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle("Example of 3 subplots")

ax1.plot([10, 20])
ax2.plot([20, 300])
ax3.plot([10, 2000])

ax1.set_ylabel("Hello")
ax2.set_ylabel("There")
ax3.set_ylabel("ogsdng")

for ax in (ax1, ax2, ax3):
    ax.grid(True)

plt.show()
