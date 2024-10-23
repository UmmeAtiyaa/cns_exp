import numpy as np

# Hill Cipher Encryption Function
def hill_cipher_encrypt(plaintext, key):
    # Convert the key into a NumPy array (key matrix)
    key_matrix = np.array(key)

    # Convert each character in the plaintext to its corresponding number (A=0, B=1, ..., Z=25)
    plaintext_vec = [ord(c) - ord('A') for c in plaintext]

    # Perform matrix multiplication and apply modulo 26 to get the encrypted values
    result = np.dot(key_matrix, plaintext_vec) % 26

    # Convert the numeric result back to characters (A=0 -> A, B=1 -> B, ..., Z=25 -> Z)
    ciphertext = ''.join(chr(int(r) + ord('A')) for r in result)

    return ciphertext

# Hill Cipher Decryption Function
def hill_cipher_decrypt(ciphertext, key):
    # Convert the key into a NumPy array (key matrix)
    key_matrix = np.array(key)

    # Calculate the inverse of the key matrix mod 26
    key_matrix_inv = np.linalg.inv(key_matrix)  # Find the inverse of the matrix
    key_matrix_inv = np.round(key_matrix_inv).astype(int)  # Round the values to integers

    # Convert the ciphertext to a vector of numbers
    ciphertext_vec = [ord(c) - ord('A') for c in ciphertext]

    # Perform matrix multiplication with the inverse key matrix, apply modulo 26, and convert back to characters
    result = np.dot(key_matrix_inv, ciphertext_vec) % 26

    # Convert the numeric result back to characters
    plaintext = ''.join(chr(int(r) + ord('A')) for r in result)

    return plaintext

# Example Test of Encryption and Decryption
plaintext = "HEL"
key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

# Encrypt the plaintext
ciphertext = hill_cipher_encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)

# Decrypt the ciphertext
# Note: The inverse key should be calculated modulo 26 for proper decryption
# This function does not yet handle modular inverses properly.
# decrypt_text = hill_cipher_decrypt(ciphertext, key)
# print("Decrypted Text: ", decrypt_text)
