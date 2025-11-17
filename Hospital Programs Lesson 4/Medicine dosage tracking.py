PATIENT_NAME = input("Enter the patient's name: ")
PATIENT_AGE = int(input("Enter the patient's age: "))
maxDosage = 0
dosageToday = int(input("Enter how much medicine the patient has had today: "))
isChild = False

if PATIENT_AGE < 18:
    isChild = True

print(PATIENT_NAME, "has taken", dosageToday, "mg today.")

if isChild == True:
    maxDosage = 300
    if dosageToday > maxDosage:
        print("Warning: The taken dosage has exceeded the safe limit!")
    else:
        print("The dosage taken is still within the safe limit.")

else:
    maxDosage = 500
    if dosageToday > maxDosage:
        print("Warning: The taken dosage has exceeded the safe limit!")
    else:
        print("The dosage taken is still within the safe limit.")
