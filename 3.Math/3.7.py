# 3.7. Write a program that read any angle t and display cosec(t)

import math

# Get input from the user
user_input = input("Enter an angle in degrees: ")

# Convert the input to a float (since angles can be fractional)
try:
    angle = float(user_input)
    # Convert the angle to radians
    radians_angle = math.radians(angle)

    # Calculate the sine and cosecant
    sine_value = math.sin(radians_angle)
    
    # Check if sine is close to zero to avoid division by zero
    if abs(sine_value) < 1e-10:
        print(f"The cosecant of {angle} degrees is undefined (division by zero).")
    else:
        cosecant_value = 1 / sine_value
        print(f"The cosecant of {angle} degrees is {cosecant_value:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
