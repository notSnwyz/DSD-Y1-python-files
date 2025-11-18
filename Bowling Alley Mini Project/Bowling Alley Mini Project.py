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

for category, items in cafeMenu.items():
    print(f"\n--- {category} ---")
    for name, price in items.items():
        print(f"{name}: £{price}")

while True:
    order = input("\nPlease enter your order (or type 'exit' to finish): ").strip()
    if order.lower() == 'exit':
        break

    found = False
    for category, items in cafeMenu.items():
        if order in items:
            print(f"You ordered: {order} - £{items[order]}")
            found = True
            break

    if not found:
        print("Item not found in the menu. Please try again.")