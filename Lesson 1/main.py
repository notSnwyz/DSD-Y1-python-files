
var1 = int(3)
var2 = float(2.4)
var3 = bool(True)
var4 = str("Hello World")
var5 = dict = {
    "Name": "Mario",
    "Age": 16
}
var6 = [1, 2, 3, 4, 8, 9, 10]

print("The difference between an integer and a float is that an integer is a whole number. For example,"
       , str(var1) + ". A float is a decimal point number. For example, " + str(var2))

x = 0

for i in range(10):
    x = x + 1
    print(x)

print("End")

for x in var6:
    print(x)
    
print("End")

squares = [ ]

for number in range(10):
    squares.append(number**2)

print(squares)



count = int(input("What number do you want you want to count to? "))

iteration = 0

for i in range(count):
    iteration = iteration + 1
    print(iteration)

