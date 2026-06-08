plaintext = "HELLO"
key = 5

ciphertext = ""

for char in plaintext:
    ciphertext += chr(ord(char) ^ key)

print("Encrypted:", ciphertext)

decrypted = ""

for char in ciphertext:
    decrypted += chr(ord(char) ^ key)

print("Decrypted:", decrypted)