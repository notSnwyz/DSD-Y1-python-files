def validate_parcel_code(code):
    if len(code) != 7 or not code.isdigit():
        return False, "Invalid format (must be exactly 7 digits)"

    first_six = code[:6]
    last_digit = int(code[6])

    total = 0
    for i in range(6):
        digit = int(first_six[i])
        total += digit * (i + 1)

    calculated_digit = total % 10

    if calculated_digit == last_digit:
        return True, "Parcel code is VALID"
    else:
        return False, "Parcel code is INVALID"

incorrect_attempts = 0

while True:
    user_input = input("Enter a 7-digit parcel code (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    is_valid, message = validate_parcel_code(user_input)
    print(message)

    if not is_valid:
        incorrect_attempts += 1

print(f"\nTotal incorrect attempts: {incorrect_attempts}")