restingHeartRate = int(input("Enter the patient's resting heart rate: "))
MAX_HEART_RATE = 220
age = int(input("Enter the patient's age: "))

safeMaxHeartRate = MAX_HEART_RATE - age

if restingHeartRate > safeMaxHeartRate:
    print("The patient's resting heart rate is abnormally high and they may be in danger")
else:
    print("The patient's resting heart rate is normal")