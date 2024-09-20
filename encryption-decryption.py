# A script that demonstrates simple encryption and decryption using the Fernet symmetric encryption method from the cryptography library.
from cryptography.fernet import Fernet

def generate_key():
    """ Generate a secure symmetric encryption key. """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """ Encrypt a message using the provided key. """
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    """ Decrypt a message using the provided key. """
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()

def main():
    key = generate_key()  # Generate a key
    print("Welcome to the simple encryption/decryption program!")
    
    # User chooses to encrypt or decrypt
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").lower()
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted = encrypt_message(message, key)
        print(f"Encrypted: {encrypted}")
    elif choice == 'd':
        message = input("Enter the message to decrypt (in bytes): ")
        # Since input is expected in bytes, convert string literal to bytes
        try:
            message_bytes = bytes(message, 'utf-8').decode('unicode_escape').encode('ISO-8859-1')
            decrypted = decrypt_message(message_bytes, key)
            print(f"Decrypted: {decrypted}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
