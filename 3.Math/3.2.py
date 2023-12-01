# 3.2. Write a program that read any angle t and display sin(t)

import math

# Get input from the user
user_input = input("Enter an angle in degrees: ")

# Convert the input to a float (since angles can be fractional)
try:
    angle = float(user_input)
    # Convert the angle to radians and calculate the sine
    sine_value = math.sin(math.radians(angle))
    print(f"The sine of {angle} degrees is {sine_value:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
