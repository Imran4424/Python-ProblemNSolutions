# 3.5. Write a program that read any angle t and display cot(t)

import math

# Get input from the user
user_input = input("Enter an angle in degrees: ")

# Convert the input to a float (since angles can be fractional)
try:
    angle = float(user_input)
    # Convert the angle to radians
    radians_angle = math.radians(angle)

    # Calculate the tangent and cotangent
    tangent_value = math.tan(radians_angle)
    
    # Check if tangent is close to zero to avoid division by zero
    if abs(tangent_value) < 1e-10:
        print(f"The cotangent of {angle} degrees is undefined (division by zero).")
    else:
        cotangent_value = 1 / tangent_value
        print(f"The cotangent of {angle} degrees is {cotangent_value:.4f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
