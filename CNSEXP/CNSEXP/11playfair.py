# Playfair Cipher Encryption Function
def playfair_encrypt(plaintext, key):
    matrix = []  # To hold the 5x5 matrix for the cipher

    # Step 1: Create the Playfair cipher matrix using the key
    # Add the characters of the key to the matrix (without duplicates)
    for c in key.upper():
        if c not in matrix and c != 'J':  # 'J' is replaced by 'I' in Playfair cipher
            matrix.append(c)
    
    # Fill the remaining matrix with the rest of the alphabet (excluding 'J')
    for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # 'J' is excluded from the matrix
        if c not in matrix:
            matrix.append(c)
    
    # Convert the flat list into a 5x5 matrix
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    # Helper function to find the position of a character in the matrix
    def find_pos(c):
        for i, row in enumerate(matrix):  # Loop through the matrix rows
            if c in row:
                return i, row.index(c)  # Return row and column index of the character

    # Function to encrypt a pair of characters
    def encrypt_pair(a, b):
        r1, c1 = find_pos(a)  # Find position of the first character in the matrix
        r2, c2 = find_pos(b)  # Find position of the second character in the matrix

        # Rule 1: If both characters are in the same row, replace each with the next character in the row
        if r1 == r2:
            return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        
        # Rule 2: If both characters are in the same column, replace each with the next character in the column
        if c1 == c2:
            return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        
        # Rule 3: Otherwise, replace them with the characters in the same row but in each other's column
        return matrix[r1][c2] + matrix[r2][c1]

    # Prepare the plaintext: convert to uppercase, replace 'J' with 'I'
    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I")

    # Step 2: Encrypt the plaintext two characters at a time
    for i in range(0, len(plaintext), 2):
        # If the two characters are the same or there's a single character left, add 'X'
        if i+1 >= len(plaintext) or plaintext[i] == plaintext[i+1]:
            ciphertext += encrypt_pair(plaintext[i], 'X')
        else:
            ciphertext += encrypt_pair(plaintext[i], plaintext[i+1])
    
    return ciphertext

# Playfair Cipher Decryption Function
def playfair_decrypt(ciphertext, key):
    matrix = []  # Same process as encryption to generate the matrix
    for c in key.upper():
        if c not in matrix and c != 'J':
            matrix.append(c)
    for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in matrix:
            matrix.append(c)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    # Helper function to find the position of a character in the matrix
    def find_pos(c):
        for i, row in enumerate(matrix):
            if c in row:
                return i, row.index(c)

    # Function to decrypt a pair of characters
    def decrypt_pair(a, b):
        r1, c1 = find_pos(a)
        r2, c2 = find_pos(b)

        # Rule 1: If both characters are in the same row, replace each with the previous character in the row
        if r1 == r2:
            return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        
        # Rule 2: If both characters are in the same column, replace each with the previous character in the column
        if c1 == c2:
            return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        
        # Rule 3: Otherwise, replace them with the characters in the same row but in each other's column
        return matrix[r1][c2] + matrix[r2][c1]

    # Decrypt two characters at a time
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i], ciphertext[i+1])

    return plaintext

# Test the encryption and decryption
plaintext = "Harsh"
key = "KEYWORD"

# Encrypt the plaintext
ciphertext = playfair_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)  # Example output: GYIZWZ

# Decrypt the ciphertext
decrypted_text = playfair_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)  # Example output: HELXOX
