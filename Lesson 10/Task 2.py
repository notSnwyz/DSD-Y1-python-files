def temp(temperature):
    if temperature > 37.5:
        print(f"You have got a fever with a temperature of {temperature}.")

def oxy(oxygen):
    if oxygen < 92:
        print("Your oxtgen levels are too low")
    
def heart_rate(heartRate):
    if heartRate >= 60 or heartRate <= 100:
        print("Heart rate normal")

temperature = float(input("Enter your temperature: "))
oxygen = int(input("Enter your oxygen levels: "))
heartRate = int(input("Enter your heart rate: "))

temp(temperature)
oxy(oxygen)
heart_rate(heartRate)