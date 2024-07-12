def encrypt_decrypt_message():
    # Input the message
    msg = input("Enter the message:\n")
    key = int(input("Enter key: "))

    # Choose the operation
    choice = int(input("Enter your choice \n1. Encryption \n2. Decryption \n"))

    if choice == 1:  # Encryption
        encrypted_message = ""
        for ch in msg:
            if 'a' <= ch <= 'z':
                ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
            elif 'A' <= ch <= 'Z':
                ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            encrypted_message += ch
        print("Encrypted message:", encrypted_message)

    elif choice == 2:  # Decryption
        decrypted_message = ""
        for ch in msg:
            if 'a' <= ch <= 'z':
                ch = chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
            elif 'A' <= ch <= 'Z':
                ch = chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
            decrypted_message += ch
        print("Decrypted message:", decrypted_message)

    else:
        print("Invalid choice")

# Call the function
encrypt_decrypt_message()
