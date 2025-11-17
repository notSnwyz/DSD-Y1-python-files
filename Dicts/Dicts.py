arcadeMachines = {
    "Pinball Wizard": {"Category": "Pinball", "Status": "Working"},
    "Retro Racer": {"Category": "Racing", "Status": "Needs Service"}
}

while True:
    option = int(input("Enter which option you want:\n1. View all machines\n2. Add a new machine\n3. Update a machine's status\n4. Delete a machine\n5. Exit\n"))

    if option == 1:  
        for name, info in arcadeMachines.items():
            print(f"\n{name}\nCategory: {info["Category"]}\nStatus: {info["Status"]}\n")

    elif option == 2:
        print("The current machines are:")
        for name in arcadeMachines:
            print(name)
        machineName = input("Enter the name of the arcare machine: ")
        machineCategory = input("Enter the category of the arcade machine: ")
        machineStatus = input("Enter the status of the arcade machine: ")

        arcadeMachines[machineName] = {"Category": machineCategory, "Status": machineStatus}
        
    elif option == 3:
        print("The current machines are:")
        for name in arcadeMachines:
            print(name)
        updateName = input("Which machine do you want to update: ")
        if updateName in arcadeMachines:
            print(f"The current status of the machine {updateName} is {arcadeMachines[updateName]["Status"]}")

            updateStatus = input("What do you want to change the status to? ")

            arcadeMachines[updateName]["Status"] = updateStatus
        
        else:
            print("Invalid machine name")
    
    elif option == 4:
        print("The current machines are:")
        for name in arcadeMachines:
            print(name)
        
        machineRemove = input("Which machine do you want to remove? ")

        if machineRemove in arcadeMachines:
            arcadeMachines.pop(machineRemove)
        else:
            print("Invalid machine")
    
    elif option == 5:
        break

