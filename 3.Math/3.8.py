# 3.8. Write a program that read a value n and display sin inverse(n)

import math

# Get input from the user
user_input = input("Enter a value for n: ")

# Convert the input to a float
try:
    n = float(user_input)
    # Check if the input value is within the valid range for arcsine
    if -1 <= n <= 1:
        # Calculate the arcsine and convert the result to degrees
        arcsine_value = math.degrees(math.asin(n))
        print(f"The arcsine of {n} is {arcsine_value:.4f} degrees")
    else:
        print("Invalid input. Please enter a value between -1 and 1.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
