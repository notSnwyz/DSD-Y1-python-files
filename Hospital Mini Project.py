

#Variables and constants for program 1
testType = ""
currentUnits = ""
CONVERSION_RATE = 18
glucose = 0.0
cholesterol = 0.0

#Variables and constants used for program 2
FEVER_LIMIT = 37.5
temperatures = []
roundedAverageTemp = 0.0

#Variables and constants used for program 3
MAX_HEART_RATE = 220
MIN_HEART_RATE = 60
restingHeartRate = 0
age = 0
safeMaxHeartRate = 0

#Variables and constants used for program 4
DAILY_WATER_GOAL = 2.0
waterIntake = 0.0
waterNeeded = 0.0

#Functions used for program 1
def glucose_to_cholesterol(glucose):
    cholesterol = glucose / CONVERSION_RATE

    return cholesterol

def cholesterol_to_glucose(cholesterol):
    glucose = cholesterol * CONVERSION_RATE

    return glucose

while True:

    programUsed = int(input("1: Lab Result Unit Converter\n2: Average Temperature Tracker\n3: Heart Rate Monitor\n4: Patient Hydration Tracker\n5. Step tracker\n6. Hydration points\n7. Hydration tracker\n8. medication tracker\n 9. Exit\nEnter the number corresponding to which program you want to use: "))
    
    if programUsed == 1:
        testType = input("Enter whether the test was for glucose or cholesterol: ")
        if testType == "glucose" or testType == "Glucose":
            currentUnits = "mg/dL"
        elif testType == "cholesterol" or testType == "Cholesterol":
            currentUnits = "mmol/L"
        else:
            print("Invalid entry")
        
        if currentUnits == "mg/dL":
            glucose = float(input("Enter the test results for glucose: "))
            cholesterol = glucose_to_cholesterol(glucose)
        elif currentUnits == "mmol/L":
            cholesterol = float(input("Enter the test results for cholesterol: "))
            glucose = cholesterol_to_glucose(cholesterol)

        print(f"The result for glucose is {glucose} mg/dL. The result for cholesterol is {cholesterol} mmol/L")

    elif programUsed == 2:
        for i in range(3):
            value = float(input(f"Enter temperature readings {i+1}: "))
            if value < 45.0 or value > 30.0:
                temperatures.append(value)
            else:
                print("Invalid temperature")


        averageTemp = sum(temperatures) / len(temperatures)

        roundedAverageTemp = round(averageTemp, 2)

        if averageTemp < FEVER_LIMIT:
            print(f"Your average temp of {averageTemp:.2f} is good as it is under the limit of {FEVER_LIMIT}")
        else:
            print(f"Warning your average temperature of {averageTemp:.2f} is over the limit of {FEVER_LIMIT}".format(averageTemp))

    elif programUsed == 3:
        restingHeartRate = int(input("Enter the patient's resting heart rate: "))
        age = int(input("Enter the patient's age: "))
        safeMaxHeartRate = MAX_HEART_RATE - age

        if restingHeartRate > safeMaxHeartRate:
            print("The patient's resting heart rate is abnormally high. Heart rate:", restingHeartRate)
        elif restingHeartRate < MIN_HEART_RATE:
            print("The patient's resting heart rate is abnormally low. Heart rate:", restingHeartRate)
        else:
            print("The patient's resting heart rate is normal. Heart rate:", restingHeartRate)
    
    elif programUsed == 4:
        waterIntake = float(input("Enter how much water the patient has had today: "))
        
        if waterIntake > DAILY_WATER_GOAL:
            print(f"You have reached the daily goal of {DAILY_WATER_GOAL} liters today. Well done!")
        else:
            waterNeeded = DAILY_WATER_GOAL - waterIntake
            print(f"The patient needs to drink {waterNeeded} more liters to reach their goal of {DAILY_WATER_GOAL} liters today.")
    
    elif programUsed == 5:
        steps = int(input("enter how many steps you have walked today: "))
        print(f"You have walked {steps} today. Keep going!")

    elif programUsed == 6:
        points = 0
        waterML = int(input("How many ML of water have you drank today? "))

        points = points + ((waterML // 2000) * 250)
        points = points + ((waterML % 2000) / 250)

    elif programUsed == 7:
        waterIntakeToday = int(input("How much water have you drank today? "))
        dailyGoal = int(input("What is your hydration goal? "))

        remaining = dailyGoal - waterIntake

        print(f"You have drank {waterIntakeToday} liters of water today and your goal is {dailyGoal} liters. You need to drink {remaining} more liters of water today.")

    elif programUsed == 8:
        break