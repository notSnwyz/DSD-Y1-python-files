#Calculate area of a rectangle
def calculate_area(width, length):
    return width * length

width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))
area = calculate_area(width, length)

print(f"The area of the rectangle is {area}")


#Convert minutes into hours
minutes = int(input("Enter the amount of minutes you want to convert to hours: "))
remainingMinutes = 0
hours = 0

def minutes_to_hours(minutes):
    hours = minutes // 60
    remainingMinutes = minutes % 60
    return hours, remainingMinutes

hours, remainingMinutes = minutes_to_hours(minutes)

print(f"{minutes} minutes = {hours} hours and {remainingMinutes} minutes")

#Billing system
def calculate_VAT(price, VAT):
    return price * VAT

VAT = 1.2
price = str(input("Enter the price of the item: "))
price = float(price)
totalPrice = calculate_VAT(price, VAT)

print(f"The total price of the item plus VAT is £{totalPrice}")

#Hospital project
name = input("Enter the patient's name: ")
age = int(input("Enter the patient's age: "))
billAmount = float(input("Enter the patient's bill for the stay: "))
VAT = 1.2 #20% VAT
DISCOUNT = 1.3 #30% discount
paymentOption = " "

billWithVAT = billAmount * VAT

if age <= 18:
    billWithVAT = billWithVAT / 1.3

if billWithVAT >= 1000:
    print("The payment options are:\nCash\nDebit Card\nCredit Card")
    paymentOption = input("What would you want to pay with? ")
    print(f"The final bill for {name} aged {age} comes out to £{billWithVAT}. They will be paying with {paymentOption}.")
else:
    print(f"The final bill for {name} aged {age} comes out to £{billWithVAT}.")

#Loops & Selection
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    option = int(input("Which option do you want? "))
    if option == 4:
        break


password = " "

while password != "Password123":
    password = input("Enter the password: ")

print("Password correct!")

#Patient Menu system
option = int(input("Which program do you want to use?\n1. Patient detail tracker\n2. BMI Calculator\n 3. Medicine dosage\n4. Exit\n"))


def calculate_bmi(height, weight):
    height = int(input("Enter your height in meters: "))
    weight = int(input("Enter your weight in KG: "))

    bmi = weight / (weight**2)
    
    return bmi

while True:
    if option == 1:
        name = input("Enter the patient's name: ")
        age = int(input("Enter the patient's age"))
        height = int(input("Enter the patient's height in CM: "))
        weight = float(input("Enter the patient's weight in KG: "))

        print(f"The patient details for {name} are:\nName: {name}\nAge: {age}\nHeight {height} CM\nWeight {weight} KG")
    
    elif option == 2:
        bmi = calculate_bmi()
        if bmi < 18.5:
            print(f"Your BMI of {bmi} indicates that you are underweight.")
        elif bmi <= 24.9 and bmi >= 18.5:
            print(f"Your BMI of {bmi} indicated that you are in a normal range.")
        elif bmi <= 29.9 and bmi >= 25:
            print(f"Your BMI of {bmi} indicated that you are overweight")
        else:
            print(f"Your BMI of {bmi} indicated that you are obese.")
    
    elif option == 3:
        MAX_DOSAGE = 500
        dosageTaken = int(input("How much medicine have you taken today? "))

        if dosageTaken > MAX_DOSAGE:
            print(f"Warning! Your dosage intake today of {dosageTaken} is over the maximum recommended dosage of {MAX_DOSAGE}.")
        else:
            print(f"Your dosage taken today of {dosageTaken} is under the maximum recommended dosage of {MAX_DOSAGE}.")