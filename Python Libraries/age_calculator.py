from datetime import datetime, date

currentTime = datetime.now()

print(f"Today's date: {currentTime.strftime("%d/%m/%y")}")

print(f"Current time: {currentTime.strftime("%H:%M:%S")}")

birthYear = int(input("Enter your birth year (YYYY): "))

currentYear = currentTime.year
age = currentYear - birthYear

print(f"You are {age} years old.")

birthMonth = int(input("Enter your birth month (1-12): "))
birthDay = int(input("Enter your birth day (1-31): "))

nextBirthday = date(currentYear, birthMonth, birthDay)

if nextBirthday < currentTime.date():
    nextBirthday = date(currentYear + 1, birthMonth, birthDay)

daysUntilBirthday = (nextBirthday - currentTime.date()).days

print(f"Days until your next birthday {daysUntilBirthday}")