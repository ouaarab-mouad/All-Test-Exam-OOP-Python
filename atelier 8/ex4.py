def frange(start, stop=None, step=1.0):
    if stop is None:  # Handle the range(stop) case.
        stop = start + 0.0  # Ensure a float value for stop
        start = 0.0
    while start < stop:
        yield round(start, 10)  # Avoiding floating point arithmetic issues
        start += step

# Exemple d'utilisation
for i in frange(5.6):
    print(i, end=", ")
print()

for i in frange(0.3, 5.6):
    print(i, end=", ")
print()

for i in frange(0.3, 5.6, 0.8):
    print(i, end=", ")
print()
