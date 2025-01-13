def read_int(prompt, min, max):
    while True:
        try:
            v = int(input(prompt))
        except ValueError:
            print("Error: bad input, please enter an integer.")
            continue

        if v < min or v > max:
            print(f"Error: the value is not within the allowed range ({min}..{max}).")
            continue

        return v
v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)         

