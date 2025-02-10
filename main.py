from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'")

# Function to load the saved key
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Please generate a key first.")
        return None

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    if key:
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        print(f"Encrypted message: {encrypted_message.decode()}")
        return encrypted_message
    return None

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    if key:
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        print(f"Decrypted message: {decrypted_message}")
        return decrypted_message
    return None

if __name__ == "__main__":
    print("Welcome to Cryptography Demo!")
    print("1. Generate Key\n2. Encrypt Message\n3. Decrypt Message\n4. Exit")

    while True:
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            message = input("Enter the message to encrypt: ")
            encrypt_message(message)
        elif choice == "3":
            encrypted_message = input("Enter the encrypted message: ").encode()
            decrypt_message(encrypted_message)
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
