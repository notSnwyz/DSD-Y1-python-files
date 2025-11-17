screenTimes = [120, 95, 140, 160, 80, 100, 200]

print(screenTimes[2])

average = (screenTimes[0] + screenTimes[1] + screenTimes[2]) / 3

print(average)

screenTimes.remove(screenTimes[-1])
screenTimes.append(500)

print(f"The highest value is {max(screenTimes)} and the lowest value is {min(screenTimes)}.")