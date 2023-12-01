# 3.4. Write a program that read any angle t and display tan(t)

import math

# Get input from the user
user_input = input("Enter an angle in degrees: ")

# Convert the input to a float (since angles can be fractional)
try:
    angle = float(user_input)
    # Convert the angle to radians and calculate the tangent
    tangent_value = math.tan(math.radians(angle))
    print(f"The tangent of {angle} degrees is {tangent_value:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")


