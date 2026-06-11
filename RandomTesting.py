import random

# Generate 100 random bits
sequence = ''.join(str(random.randint(0,1)) for _ in range(100))

print("Generated Sequence:")
print(sequence)

# ------------------------
# Frequency Test
# ------------------------
zeros = sequence.count('0')
ones = sequence.count('1')

print("\nFREQUENCY TEST")
print("Zeros =", zeros)
print("Ones =", ones)

if abs(zeros - ones) <= 10:
    print("Interpretation: Sequence appears balanced.")
else:
    print("Interpretation: Sequence may not be random.")

# ------------------------
# Runs Test
# ------------------------
runs = 1

for i in range(1, len(sequence)):
    if sequence[i] != sequence[i-1]:
        runs += 1

print("\nRUNS TEST")
print("Number of Runs =", runs)

if 40 <= runs <= 60:
    print("Interpretation: Runs appear random.")
else:
    print("Interpretation: Too many or too few runs.")

# ------------------------
# Mean Test
# ------------------------
numbers = [int(bit) for bit in sequence]
mean = sum(numbers) / len(numbers)

print("\nMEAN TEST")
print("Mean =", mean)

if 0.45 <= mean <= 0.55:
    print("Interpretation: Mean is close to expected value.")
else:
    print("Interpretation: Mean indicates possible bias.")