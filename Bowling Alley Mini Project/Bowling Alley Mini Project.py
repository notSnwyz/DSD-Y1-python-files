cafeMenu = {
    "Drinks": {
        "Coffee": 2.49,
        "Coca Cola": 1.99,
        "Fanta": 1.99,
        "Lipton": 1.99,
        "Tea": 2.49
    },
    "Mains": {
        "Fish and Chips": 7.99,
        "Pizza": 8.99,
        "Lasagna": 9.99,
        "Spaghetti Bolognese": 9.99
    },
    "Deserts": {
        "Vanilla Ice Cream": 3.99,
        "Chocolate Ice Cream": 3.99,
        "Strawberry Ice Cream": 3.99,
        "Brownie": 2.49,
        "Brownie with Ice Cream": 6.99
    }
}

def listMenu():
    for category, items in cafeMenu.items():
        print(f"\n--- {category} ---")
        for name, price in items.items():
            print(f"{name}: £{price}")


newCustomer = input("Is this person a new customer? ")
pricePerPerson = 0
totalPrice = 0




if newCustomer.lower() == "yes":

    print("The bowling alley is open from 12pm to 10pm.")
    timeOfBooking = input("What time are you booking for? ")

    print("The price per person is £15 but there is a 20% discount for bookings with 4 or more people.")
    people = int(input("How many people are you booking for? "))

    if people >= 4:
        pricePerPerson = 15 * 0.8
    else:
        pricePerPerson = 15
    
    totalPrice = pricePerPerson * people
    print(f"The total price for your booking of {people} people at {timeOfBooking}pm is £{totalPrice:.2f}.")

