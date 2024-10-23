def vigenere_encrypt(plaintext, key):
    # Step 1: Repeat the key to match the length of the plaintext
    key = (key * len(plaintext))[:len(plaintext)]  # Repeat the key and slice it to the plaintext length
    ciphertext = ''  # Initialize an empty string for the ciphertext
    
    # Step 2: Encrypt each character of the plaintext
    for i in range(len(plaintext)):
        # Calculate the encrypted character using the formula
        c = (ord(plaintext[i]) + ord(key[i]) - 2 * ord('A')) % 26  # Vigenère encryption formula
        ciphertext += chr(c + ord('A'))  # Append the encrypted character to the ciphertext
    
    return ciphertext  # Return the complete ciphertext

def vigenere_decrypt(ciphertext, key):
    # Step 1: Repeat the key to match the length of the ciphertext
    key = (key * len(ciphertext))[:len(ciphertext)]  # Repeat the key and slice it to the ciphertext length
    plaintext = ''  # Initialize an empty string for the decrypted plaintext
    
    # Step 2: Decrypt each character of the ciphertext
    for i in range(len(ciphertext)):
        # Calculate the decrypted character using the formula
        p = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26  # Vigenère decryption formula
        plaintext += chr(p + ord('A'))  # Append the decrypted character to the plaintext
    
    return plaintext  # Return the complete plaintext

# Example Usage:
plaintext = "HELLO"  # Message to encrypt
key = "KEY"  # Key for encryption

# Encrypt the plaintext
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted:", ciphertext)  # Display the ciphertext

# Decrypt the ciphertext
decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)  # Display the decrypted plaintext
