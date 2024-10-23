# Autokey Cipher Encryption Function
def autokey_encrypt(plaintext, key):
    # Extend the key by appending part of the plaintext (not the whole)
    key_extended = key + plaintext  # This generates the extended key
    key_extended = key_extended[:len(plaintext)]  # Key is trimmed to match plaintext length
    
    ciphertext = ''  # Initialize ciphertext

    # Encrypt each character of plaintext
    for i in range(len(plaintext)):
        # Calculate the position of ciphertext character
        c = (ord(plaintext[i]) + ord(key_extended[i]) - 2 * ord('A')) % 26
        ciphertext += chr(c + ord('A'))  # Convert back to letter and add to ciphertext

    return ciphertext

# Autokey Cipher Decryption Function
def autokey_decrypt(ciphertext, key):
    plaintext = ''  # Initialize plaintext

    # Decrypt each character of ciphertext
    for i in range(len(ciphertext)):
        # Calculate the position of plaintext character
        p = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        decrypted_char = chr(p + ord('A'))  # Convert back to letter
        plaintext += decrypted_char  # Add decrypted letter to plaintext
        
        # Extend the key with the newly decrypted character (for subsequent characters)
        key += decrypted_char

    return plaintext

# Test the encryption and decryption functions
plaintext = "HELLO"
key = "KEY"

# Encrypt the plaintext
ciphertext = autokey_encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)

# Decrypt the ciphertext
decrypted_text = autokey_decrypt(ciphertext, key)
print("Decrypted Text: ", decrypted_text)
