DAILY_WATER_GOAL = 2.0
dailyWaterIntake = float(input("Enter the patient's water intake for the day: "))

if dailyWaterIntake >= DAILY_WATER_GOAL:
    print("Hydration goal achieved!")
else:
    print("The patient needs more water.")