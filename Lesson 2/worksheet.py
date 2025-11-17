firstName = input("Enter your first name ")
print("Hello " + firstName)

surname = input("Enter your surname ")
print("Your surname is " + surname)

print("Hello " + firstName + " " + surname)

print("Your initials are: " + firstName[0] + " " + surname[0])

fullName = firstName + surname

print(surname.upper() + firstName)

print("You have " + str(len(firstName)) + " letters in your first name. In your surname you have "
       + str(len(surname)) + " letters")

def createUserName():
    return surname[0:3] + firstName[0] + str(len(surname))

userName = createUserName()

print(userName)