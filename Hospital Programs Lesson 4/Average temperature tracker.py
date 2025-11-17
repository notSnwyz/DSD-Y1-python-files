FEVER_LIMIT = 37.5
temperatures = []
for i in range(3):
    value = float(input(f"Enter temperature readings {i+1}: "))
    temperatures.append(value)
averageTemp = sum(temperatures) / len(temperatures)

if averageTemp > FEVER_LIMIT:
    print(f"Warning your average temperature of {averageTemp} is over the limit of {FEVER_LIMIT}")
else:
    print(f"Your average temp of {averageTemp} is good as it is under the limit of {FEVER_LIMIT}")