# 3.10. Write a program that read a value n and display tan inverse(n)

import math

# Get input from the user
user_input = input("Enter a value for n: ")

# Convert the input to a float
try:
    n = float(user_input)
    # Calculate the arctangent and convert the result to degrees
    arctangent_value = math.degrees(math.atan(n))
    print(f"The arctangent of {n} is {arctangent_value:.4f} degrees")

except ValueError:
    print("Invalid input. Please enter a valid number.")
