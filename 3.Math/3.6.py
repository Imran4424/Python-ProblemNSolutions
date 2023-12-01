# 3.6. Write a program that read any angle t and display sec(t)

import math

# Get input from the user
user_input = input("Enter an angle in degrees: ")

# Convert the input to a float (since angles can be fractional)
try:
    angle = float(user_input)
    # Convert the angle to radians
    radians_angle = math.radians(angle)

    # Calculate the cosine and secant
    cosine_value = math.cos(radians_angle)
    
    # Check if cosine is close to zero to avoid division by zero
    if abs(cosine_value) < 1e-10:
        print(f"The secant of {angle} degrees is undefined (division by zero).")
    else:
        secant_value = 1 / cosine_value
        print(f"The secant of {angle} degrees is {secant_value:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
