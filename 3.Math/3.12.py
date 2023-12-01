# 3.12. Write a program that read a value n and display sec inverse(n)

import math

# Get input from the user
user_input = input("Enter a value for n: ")

# Convert the input to a float
try:
    n = float(user_input)
    # Check if the input value is within the valid range for arcsecant
    if -1 <= n <= 1 and n != 0:
        # Calculate the arccosine of the reciprocal of the value and convert the result to degrees
        arcsecant_value = math.degrees(math.acos(1 / n))
        print(f"The arcsecant of {n} is {arcsecant_value:.4f} degrees")
    else:
        print("Invalid input. The arcsecant is undefined for values outside the range (-1 to 1) or for zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
