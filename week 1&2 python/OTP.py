import random
import string

plaintext = "HELLO"

key = ''.join(random.choice(string.ascii_uppercase)
              for _ in range(len(plaintext)))

print("Key:", key)

cipher = ""

for p, k in zip(plaintext, key):
    c = (ord(p)-65 + ord(k)-65) % 26
    cipher += chr(c + 65)

print("Ciphertext:", cipher)