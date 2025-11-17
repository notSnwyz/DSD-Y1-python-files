
def calorie_burn(caloriesPerMinute, workoutTime):
    return caloriesPerMinute * workoutTime

def steps_conversion(steps):
    return steps / 1300

def medical_timing(minutes):
    hours = minutes // 60
    remainingMinutes = minutes % 60
    return hours, remainingMinutes

def remaining_medication(totalMedication, medicationUsed):
    return totalMedication - medicationUsed




while True:
    option = int(input("Enter which program you want:\n1. Calorie burn calculator\n2. Step conversion\n3. Medical timing\n4. Medicine pack usage\n5. Heart recovery\n6. Exit\n"))
    if option == 1:
        caloriesPerMinute = int(input("How many calories did you burn per minute? "))
        workoutTime = int(input("How many minutes did you work out? "))

        print(f"Your total calorie burn is {calorie_burn(caloriesPerMinute, workoutTime)}")
    elif option == 2:
        steps = int(input("How many steps did you walk today? "))
        print(f"Your entered steps are approximately {steps_conversion(steps):.2} kilometers")
                
    elif option == 3:
        minutes = int(input("Enter how many minutes you want to convert: "))
        hours, remainingMinutes = medical_timing(minutes)

        print(f"{minutes} minutes = {hours} hours and {remainingMinutes} minutes")
                
    elif option == 4:
        totalMedication = int(input("Enter how much medication you have in the pack: "))
        medicationUsed = int(input("Enter how much medication you have used from the pack: "))
        print(f"Out of the {totalMedication} tablets in the pack, you have used {medicationUsed} tablets. Therefore, you have {remaining_medication(totalMedication, medicationUsed)} tablets left.")

    elif option == 5:
        print()

    elif option == 6:
        break
