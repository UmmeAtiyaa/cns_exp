def gcd(a, b):
    # Function to compute the greatest common divisor (GCD) using the Euclidean algorithm
    while b:
        a, b = b, a % b  # Update a and b until b becomes zero
    return a  # Return the GCD

def mod_inverse(a, m):
    # Function to find the modular inverse of a under modulo m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x  # Return the modular inverse if found
    return None  # Return None if no modular inverse exists

def affine_encrypt(plaintext, a, b):
    # Encrypt the plaintext using the Affine cipher
    if gcd(a, 26) != 1:  # Check if 'a' is coprime to 26
        raise ValueError("a and 26 must be coprime.")  # Raise an error if not

    ciphertext = ''  # Initialize an empty string for the ciphertext

    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Apply the Affine cipher formula: E(x) = (ax + b) mod 26
            x = ord(char.upper()) - ord('A')  # Convert letter to numeric (0-25)
            encrypted_char = (a * x + b) % 26  # Encrypt the character
            ciphertext += chr(encrypted_char + ord('A'))  # Convert back to letter and add to ciphertext
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged

    return ciphertext  # Return the complete ciphertext

def affine_decrypt(ciphertext, a, b):
    # Decrypt the ciphertext using the Affine cipher
    if gcd(a, 26) != 1:  # Check if 'a' is coprime to 26
        raise ValueError("a and 26 must be coprime.")  # Raise an error if not

    # Find the modular inverse of 'a' under modulo 26
    a_inv = mod_inverse(a, 26)  
    if a_inv is None:
        raise ValueError("Modular inverse does not exist.")  # Raise an error if no inverse exists

    plaintext = ''  # Initialize an empty string for the decrypted plaintext

    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Apply the Affine cipher formula: D(y) = a_inv * (y - b) mod 26
            y = ord(char.upper()) - ord('A')  # Convert letter to numeric (0-25)
            decrypted_char = (a_inv * (y - b)) % 26  # Decrypt the character
            plaintext += chr(decrypted_char + ord('A'))  # Convert back to letter and add to plaintext
        else:
            plaintext += char  # Non-alphabet characters remain unchanged

    return plaintext  # Return the complete plaintext

# Example Usage:
plaintext = "HELLO WORLD"  # Message to encrypt
a = 5  # 'a' must be coprime to 26
b = 8  # Shift value

# Encrypt the plaintext
ciphertext = affine_encrypt(plaintext, a, b)
print("Encrypted:", ciphertext)  # Display the ciphertext

# Decrypt the ciphertext
decrypted_text = affine_decrypt(ciphertext, a, b)
print("Decrypted:", decrypted_text)  # Display the decrypted plaintext
