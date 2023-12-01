# 3.9. Write a program that read a value n and display cos inverse(n)

import math

# Get input from the user
user_input = input("Enter a value for n: ")

# Convert the input to a float
try:
    n = float(user_input)
    # Check if the input value is within the valid range for arccosine
    if -1 <= n <= 1:
        # Calculate the arccosine and convert the result to degrees
        arccosine_value = math.degrees(math.acos(n))
        print(f"The arccosine of {n} is {arccosine_value:.4f} degrees")
    else:
        print("Invalid input. Please enter a value between -1 and 1.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
