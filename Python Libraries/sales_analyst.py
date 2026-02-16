import numpy as np

sales = np.array([120, 135, 150, 98, 175, 200, 143])

meanValues = np.mean(sales)
totalValue = np.sum(sales)
highestValue = np.max(sales)
lowestValue = np.min(sales)

print(f"Weekly Sales Data: {sales}")
print(f"Mean: {meanValues}")
print(f"Total: {totalValue}")
print(f"Highest Value: {highestValue}")
print(f"Lowest Value: {lowestValue}")

updatedSales = sales * 1.10
print(f"Updates Sales: {updatedSales}")

randomNumbers = np.random.rand(100)
randomMean = np.mean(randomNumbers)
randomStd = np.std(randomNumbers)

print(f"Random Numbers Mean: {randomMean}")
print(f"Random Numbers Standard Deviation: {randomStd}")