# A python program to illustrate Caesar Cipher Technique

# Encryption function
def encrypt(text, s):
    result = ""

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + s) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)

        # Leave non-alphabetic characters as they are
        else:
            result += char

    return result

# Decryption function
def decrypt(cipher, s):
    result = ""

    # Traverse cipher
    for i in range(len(cipher)):
        char = cipher[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 - s) % 26 + 65)

        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 - s) % 26 + 97)

        # Leave non-alphabetic characters as they are
        else:
            result += char

    return result

# Check the above functions
text = "HelloWorld"
s = 5

print("Original Text : " + text)
print("Shift         : " + str(s))

# Encrypt the text
cipher = encrypt(text, s)
print("Encrypted Text: " + cipher)

# Decrypt the text
decrypted_text = decrypt(cipher, s)
print("Decrypted Text: " + decrypted_text)
