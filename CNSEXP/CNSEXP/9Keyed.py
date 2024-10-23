# Keyed Transposition Cipher Encryption Function
def keyed_transposition_encrypt(plaintext, key):
    num_cols = len(key)  # The number of columns is determined by the length of the key
    num_rows = (len(plaintext) + num_cols - 1) // num_cols  # Calculate number of rows (rounding up)
    
    # Create an empty grid to store columns of the transposed text
    grid = [''] * num_cols

    # Fill the grid by placing each character in the appropriate column based on the key
    for i, char in enumerate(plaintext):
        # Place the character in the correct column based on the key's value
        grid[int(key[i % num_cols]) - 1] += char

    # Concatenate all columns to form the ciphertext
    return ''.join(grid)

# Keyed Transposition Cipher Decryption Function
def keyed_transposition_decrypt(ciphertext, key):
    num_cols = len(key)  # The number of columns is the length of the key
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols  # Calculate number of rows (rounding up)
    
    # Calculate the number of characters in each column
    col_lengths = [num_rows] * num_cols
    extra_chars = len(ciphertext) % num_cols  # Handle uneven divisions
    
    # Reduce the length of columns that will have fewer characters
    for i in range(extra_chars, num_cols):
        col_lengths[i] -= 1
    
    # Create an empty grid to hold the columns
    grid = [''] * num_cols
    index = 0

    # Fill the grid based on the length of each column
    for i in range(num_cols):
        col_idx = int(key[i]) - 1  # Column index from the key
        grid[col_idx] = ciphertext[index:index + col_lengths[col_idx]]  # Assign characters to each column
        index += col_lengths[col_idx]

    # Reconstruct the plaintext by reading row by row
    plaintext = ''
    for i in range(num_rows):
        for j in range(num_cols):
            if i < len(grid[j]):  # Make sure we don't read beyond the end of a shorter column
                plaintext += grid[j][i]

    return plaintext

# Test the encryption and decryption functions
plaintext = "HELLO"
key = "45213"

# Encrypt the plaintext
ciphertext = keyed_transposition_encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)

# Decrypt the ciphertext
decrypted_text = keyed_transposition_decrypt(ciphertext, key)
print("Decrypted Text: ", plaintext)
