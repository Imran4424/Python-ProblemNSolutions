# 3.13. Write a program that read a value n and display cosec inverse(n)

import math

# Get input from the user
user_input = input("Enter a value for n: ")

# Convert the input to a float
try:
    n = float(user_input)
    # Check if the input value is not zero
    if n != 0:
        # Calculate the arcsine of the reciprocal of the value and convert the result to degrees
        arccosecant_value = math.degrees(math.asin(1 / n))
        print(f"The arccosecant of {n} is {arccosecant_value:.4f} degrees")
    else:
        print("Invalid input. The arccosecant is undefined for zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
