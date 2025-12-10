def get_key():
    while True:
        key = int(input("Enter the encryption key. 1-26: "))
        if key <=26 and key >=1:
            break
        else:
            print("Not a number between 1 and 26. Try again.")
    return key

def get_message():
    return input("Enter the message you want to encrypt: ")

def get_encrypted_message():
    return input("Enter the encrypted message: ")

def encrypt_message(key, message):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

def decrypt_message(key, encryptedMessage):
    result = ""
    for char in encryptedMessage:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result

def main():
    while True:
        option = int(input("Options:\n1. Encrypt message\n2. Decrypt message\n3. Exit\n"))
        if option == 1:
            key = get_key()
            message = get_message()

            encryptedMessage = encrypt_message(key, message)

            print(f"{message} encrypted is {encryptedMessage}.")
        
        elif option == 2:
            key = get_key()
            encryptedMessage = get_encrypted_message()

            message = decrypt_message(key, encryptedMessage)

            print(f"{encryptedMessage} decrypted is {message}.")
        
        elif option == 3:
            break

main()
    