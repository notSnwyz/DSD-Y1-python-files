import math

num1 = int(input("Enter a number: "))
squareRoot = math.sqrt(num1)
squared = math.pow(num1, 2)
roundedUp =  math.ceil(num1)
roundedDown = math.floor(num1)
area = math.pi * math.pow(num1, 2)

print(f"Square Root: {squareRoot}")
print(f"Squared: {squared}")
print(f"Rounded Up: {roundedUp}")
print(f"Rounded Down: {roundedDown}")
print(f"Area: {area}")