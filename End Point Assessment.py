# steps = int(input("Enter how many steps you have taken: "))
# goal = int(input("Enter what your goal is: "))
# percentageOfGoal = (steps/goal) * 100
# remainingSteps = goal - steps

# if percentageOfGoal >= 0 and percentageOfGoal <= 100 and remainingSteps >= 0:
#     print(f"You have completed {int(percentageOfGoal)}% of your goal. You need {remainingSteps} more steps to reach it.")

# else:
#     print("Invalid")

# weightKG = float(input("Enter your weight in KG: "))
# heightM = float(input("Enter your height in meters: "))

# BMI = weightKG / (heightM ** 2)

# if BMI <= 18.5:
#     print("Underweight")

# elif BMI <= 25:
#     print("Healthy")

# elif BMI <= 30:
#     print("Overweight")

# else:
#     print("Obese")

# def flag_user(dailyScreenTime, nightScreenTime, steps):
#     return dailyScreenTime > 240 and steps < 5000 or nightScreenTime > 60

# dailyScreenTime = int(input("Enter your daily screen time: "))
# steps = int(input("How many steps have you walked today: "))
# nightScreenTime = int(input("How much screen time did you have at night: "))

# if flag_user(dailyScreenTime, nightScreenTime, steps) == True:
#     print("User flagged.")

# else:
#     print("User has not been flagged.")

# waterIntake = int(input("How many ml of water did you drink today: "))
# points = 0
# points = points + ((waterIntake // 2000 ) * 250)
# points = points + ((waterIntake % 2000) // 250)

# print(f"You have drank {waterIntake}ml of water so you now have {points} points!")

# def eligible_for_free_class(age, lowIncome, daysSinceFreeClass):
#     return age >= 16 and age <= 25 or lowIncome.lower() == "yes" and daysSinceFreeClass > 30


# age = int(input("How old are you? "))
# lowIncome = input("Are you a registered low-income participant? ")
# daysSinceFreeClass = int(input("How many days has it been since you last had a free class? "))

# if eligible_for_free_class(age, lowIncome, daysSinceFreeClass) == True:
#     print("Eligible for free classes.")

# else:
#     print("Not eligible for free classes.")

# def weekly_tier(steps, waterML):
#     points = (steps // 1000) * 2 + (waterML // 500)
#     if points <= 19:
#         return "Bronze Tier"
#     elif points <= 39:
#         return "SIlver Tier"
#     else:
#         return "Gold Tier"

# steps = int(input("How many steps did you take today? "))
# waterML = int(input("How many ml of water did you drink today? "))

# print(weekly_tier(steps, waterML))

