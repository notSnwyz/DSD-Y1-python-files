def get_middle_index(lst):
    return len(lst) // 2

energyLevels = [2, 4, 6, 5, 8]
usernames = ["mario", "kye", "bob"]
stepCount = [4203, 5670, 2043, 5360, 4305, 3658, 6830]

print(energyLevels, usernames, stepCount)

print(
    energyLevels[0], energyLevels[get_middle_index(energyLevels)], energyLevels[-1],
    usernames[0], usernames[get_middle_index(usernames)], usernames[-1],
    stepCount[0], stepCount[get_middle_index(stepCount)], stepCount[-1]
)

energyLevels.append(3)
usernames.append("sss")
stepCount.append(3050)

print(energyLevels, usernames, stepCount)

print(
    energyLevels[0], energyLevels[get_middle_index(energyLevels)], energyLevels[-1],
    usernames[0], usernames[get_middle_index(usernames)], usernames[-1],
    stepCount[0], stepCount[get_middle_index(stepCount)], stepCount[-1]
)
