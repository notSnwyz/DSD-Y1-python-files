fName = input("Enter your first name: ")
lName = input("Enter your last name: ")

fullName = fName + " " + lName

length = len(fullName)

if length >= 21:
    print("Invalid name. Make sure it's less than 20 characters")

else:
    print("Your name is " , fullName)