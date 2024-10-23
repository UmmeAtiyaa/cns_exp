# Multiplicative Cipher Encryption Function
def multiplicative_encrypt(plaintext, key):
    result = ""  # Initialize the encrypted text as an empty string
    
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter (ignores spaces and punctuation)
            num = ord(char.lower()) - ord('a')  # Convert letter to a number (0-25)
            encrypted_num = (num * key) % 26  # Multiply by key and apply modulo 26
            encrypted_char = chr(encrypted_num + ord('a'))  # Convert back to a character
            result += encrypted_char
        else:
            result += char  # Non-alphabet characters remain unchanged (like spaces or punctuation)

    return result

# Function to find the Multiplicative Inverse of key modulo 26
def multiplicative_inverse(key, mod=26):
    for i in range(1, mod):
        if (key * i) % mod == 1:
            return i
    return None  # No inverse exists if key is not coprime with 26

# Multiplicative Cipher Decryption Function
def multiplicative_decrypt(ciphertext, key):
    inverse_key = multiplicative_inverse(key)  # Find the multiplicative inverse of the key
    if inverse_key is None:
        return "Decryption is not possible with this key!"  # Key must be coprime with 26

    result = ""  # Initialize the decrypted text as an empty string
    
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            num = ord(char.lower()) - ord('a')  # Convert letter to a number (0-25)
            decrypted_num = (num * inverse_key) % 26  # Multiply by the inverse key and apply mod 26
            decrypted_char = chr(decrypted_num + ord('a'))  # Convert back to a character
            result += decrypted_char
        else:
            result += char  # Non-alphabet characters remain unchanged

    return result

# Test the encryption and decryption
plaintext = "wor"
key = 5  # Fixed key for encryption

# Encrypt the plaintext
encrypted_text = multiplicative_encrypt(plaintext, key)
print("Plain Text:", plaintext)
print("Encrypted Text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = multiplicative_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
