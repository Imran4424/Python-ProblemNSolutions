# 3.11. Write a program that read a value n and display cot inverse(n)

import math

# Get input from the user
user_input = input("Enter a value for n: ")

# Convert the input to a float
try:
    n = float(user_input)
    # Check if the input value is not zero
    if n != 0:
        # Calculate the arctangent of the reciprocal of the value and convert the result to degrees
        arccotangent_value = math.degrees(math.atan(1 / n))
        print(f"The arccotangent of {n} is {arccotangent_value:.4f} degrees")
    else:
        print("Invalid input. The arccotangent is undefined for zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")