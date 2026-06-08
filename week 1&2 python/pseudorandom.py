# Pseudorandom Sequence Generator (Auto Mode)

a = 5
c = 3
m = 16

# Use fixed seed instead of asking for input
seed = 7  # You can change this value manually
print(f"Using seed value: {seed}")

x = seed

print("\nGenerated Sequence:")

sequence = []
for i in range(20):
    x = (a * x + c) % m
    sequence.append(x)
    print(f"{i+1:2d}: {x}")

print("\nSequence as list:", sequence)
print("\nProgram Finished")
input("Press Enter to close...")