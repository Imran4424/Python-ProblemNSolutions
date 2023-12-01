# 3.3. Write a program that read any angle t and display cos(t)

import math

# Get input from the user
user_input = input("Enter an angle in degrees: ")

# Convert the input to a float (since angles can be fractional)
try:
    angle = float(user_input)
    # Convert the angle to radians and calculate the cosine
    cosine_value = math.cos(math.radians(angle))
    print(f"The cosine of {angle} degrees is {cosine_value:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")