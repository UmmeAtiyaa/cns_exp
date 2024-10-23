def gcd(a, b):
    # Function to compute the greatest common divisor (GCD) using the Euclidean algorithm
    while b:
        a, b = b, a % b  # Update a and b until b becomes zero
    return a  # Return the GCD

def rsa_keygen(p, q):
    # Function to generate RSA public and private keys
    n = p * q  # Calculate n, the modulus for the public and private keys
    
    phi = (p - 1) * (q - 1)  # Calculate Euler's totient function
    
    e = 2  # Start with a small integer e
    # Find an e such that 1 < e < phi and gcd(e, phi) = 1
    while e < phi and gcd(e, phi) != 1:
        e += 1  # Increment e until we find a suitable one
    
    # Calculate d, the modular inverse of e (d * e ≡ 1 (mod phi))
    d = pow(e, -1, phi)  
    return (e, n), (d, n)  # Return public key (e, n) and private key (d, n)

def rsa_encrypt(plaintext, public_key):
    # Function to encrypt plaintext using the public key
    e, n = public_key  # Unpack the public key
    # Encrypt each character in the plaintext using the formula: c = (p^e) mod n
    return [pow(ord(char), e, n) for char in plaintext]  # Return the ciphertext as a list of integers

def rsa_decrypt(ciphertext, private_key):
    # Function to decrypt ciphertext using the private key
    d, n = private_key  # Unpack the private key
    # Decrypt each integer in the ciphertext using the formula: p = (c^d) mod n
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])  # Return the plaintext as a string

# Example Usage:
p = 61  # Example prime number
q = 53  # Another example prime number
public_key, private_key = rsa_keygen(p, q)  # Generate the public and private keys

plaintext = "HELLO"  # Message to encrypt
ciphertext = rsa_encrypt(plaintext, public_key)  # Encrypt the plaintext
print("Encrypted:", ciphertext)  # Display the ciphertext

decrypted_text = rsa_decrypt(ciphertext, private_key)  # Decrypt the ciphertext
print("Decrypted:", decrypted_text)  # Display the decrypted plaintext
