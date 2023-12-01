# 3.16. Write a program that read any number x and display e^x

import math

# Get input from the user
x_input = input("Enter a number x: ")

# Convert the input to a float
try:
    x = float(x_input)

    # Calculate and display e^x
    result = math.exp(x)
    print(f"e^{x} is: {result:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
