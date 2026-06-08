# TRUE XOR STREAM CIPHER (with keystream)

print("=" * 50)
print("TRUE XOR STREAM CIPHER")
print("=" * 50)

message = input("\nEnter a sentence: ")
key_stream = input("Enter keystream (e.g., 'SECRET'): ")

print("\n" + "-" * 50)

# Generate keystream same length as message
keystream = (key_stream * (len(message) // len(key_stream) + 1))[:len(message)]

# ENCRYPTION
ciphertext = ""
print("\n[ENCRYPTION]")

for i, char in enumerate(message):
    if char == " ":
        ciphertext += " "
        print(f"  Position {i}: Space (unchanged)")
    else:
        key_char = ord(keystream[i])
        encrypted_char = chr(ord(char) ^ key_char)
        ciphertext += encrypted_char
        print(f"  Position {i}: '{char}' XOR '{keystream[i]}' (ord:{key_char}) → '{encrypted_char}'")

print("\n" + "-" * 50)
print(f"ENCRYPTED: {ciphertext}")

# DECRYPTION
decrypted = ""
print("\n[DECRYPTION]")

for i, char in enumerate(ciphertext):
    if char == " ":
        decrypted += " "
        print(f"  Position {i}: Space (unchanged)")
    else:
        key_char = ord(keystream[i])
        decrypted_char = chr(ord(char) ^ key_char)
        decrypted += decrypted_char
        print(f"  Position {i}: '{char}' XOR '{keystream[i]}' (ord:{key_char}) → '{decrypted_char}'")

print("\n" + "-" * 50)
print(f"DECRYPTED: {decrypted}")

if message == decrypted:
    print("\n✓ SUCCESS!")
else:
    print("\n✗ FAILED!")