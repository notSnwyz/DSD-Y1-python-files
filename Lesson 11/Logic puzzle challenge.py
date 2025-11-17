

while True:
    option = int(input("Options:\n1. Medication Safety Rule\n2. Fitness Centre Access\n3. Sleep Tracker Alert\n4. Exit\n"))
    if option == 1:
        age = int(input("Enter your age: "))
        weight = int(input("Enter your weight in KG: "))
        if age >= 12 and weight >= 40:
            print("It is safe for the person to take medication.")
        else:
            print("It is not safe for the person to take medication.")
    
    elif option == 2:
        age = int(input("Enter your age: "))
        medicalClearance = input("Do you have medical clearance to access the intensive zone? ")
        if age >= 18 and medicalClearance.lower() == "yes":
            print("You can access the intensive zone!")
        
        else:
            print("You cannot access the intensive zone.")
        
    elif option == 3:
        asleep = input("Is the person sleeping? ")
        heartRate = int(input("Enter your heart rate: "))

        if asleep.lower() == "yes" and heartRate > 100:
            print("Not Sleeping")
        
        else:
            print("Sleeping")
    
    elif option == 4:
        break