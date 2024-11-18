def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            encrypted += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            encrypted += char
    return encrypted


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    while True:
        choice = input("Do you want to (1) Encrypt, (2) Decrypt, or (3) Exit? ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print(f"Encrypted text: {encrypt(text, shift)}")

        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            print(f"Decrypted text: {decrypt(text, shift)}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
