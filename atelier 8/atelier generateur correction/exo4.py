def frange(start, stop=None, step=1.0):
    if stop is None:
        stop = start
        start = 0.0
    while start < stop:
        yield start
        start += step

# Test du générateur avec différentes configurations
print("Test 1:")
for i in frange(5.6):
    print(i, end=", ")
print("\nTest 2:")
for i in frange(0.3, 5.6):
    print(i, end=", ")
print("\nTest 3:")
for i in frange(0.3, 5.6, 0.8):
    print(i, end=", ")
print()
