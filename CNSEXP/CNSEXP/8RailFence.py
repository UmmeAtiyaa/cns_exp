# Rail Fence Cipher Encryption Function
def rail_fence_encrypt(plaintext, rails):
    # Initialize a list of strings for each rail
    rail = [''] * rails
    row = 0  # Start at the first rail
    down = True  # Direction flag for zigzag movement

    # Step 1: Arrange characters in rails
    for char in plaintext:
        rail[row] += char  # Place the character in the current rail
        # Move up or down the rails
        if down:
            row += 1  # Move down to the next rail
        else:
            row -= 1  # Move up to the previous rail
        # Change direction at the top or bottom rail
        if row == 0 or row == rails - 1:
            down = not down  # Toggle direction

    # Join all rails to form the ciphertext
    return ''.join(rail)

# Rail Fence Cipher Decryption Function
def rail_fence_decrypt(ciphertext, rails):
    # Calculate the length of each rail
    rail_lengths = [0] * rails
    row = 0  # Start at the first rail
    down = True  # Direction flag for zigzag movement

    # Step 1: Determine the length of each rail
    for char in ciphertext:
        rail_lengths[row] += 1  # Count characters for the current rail
        if down:
            row += 1
        else:
            row -= 1
        if row == 0 or row == rails - 1:
            down = not down  # Toggle direction

    # Step 2: Create a list to hold the rails
    rail = [''] * rails
    index = 0  # Start filling the rails with characters from ciphertext
    for i in range(rails):
        rail[i] = ciphertext[index:index + rail_lengths[i]]  # Fill each rail
        index += rail_lengths[i]  # Move to the next part of the ciphertext

    # Step 3: Reconstruct the plaintext from the rails
    result = []
    row = 0  # Start at the first rail
    down = True  # Direction flag for zigzag movement
    for i in range(len(ciphertext)):
        result.append(rail[row][0])  # Add the next character from the current rail
        rail[row] = rail[row][1:]  # Remove the character from the rail
        # Move up or down the rails
        if down:
            row += 1  # Move down to the next rail
        else:
            row -= 1  # Move up to the previous rail
        # Change direction at the top or bottom rail
        if row == 0 or row == rails - 1:
            down = not down  # Toggle direction

    return ''.join(result)

# Test the encryption and decryption
plaintext = "HELLO"
rails = 2

# Encrypt the plaintext
ciphertext = rail_fence_encrypt(plaintext, rails)
print("Ciphertext:", ciphertext)  # Example output: HLOEL

# Decrypt the ciphertext
decrypted_text = rail_fence_decrypt(ciphertext, rails)
print("Decrypted Text:", decrypted_text)  # Example output: HELLO
