# 3.17. Write a program that read any number x and display log(x)

import math

# Get input from the user
x_input = input("Enter a number x: ")

# Convert the input to a float
try:
    x = float(x_input)

    # Check if the number is positive before calculating the logarithm
    if x > 0:
        # Calculate and display log(x)
        result = math.log(x)
        print(f"The natural logarithm of {x} is: {result:.4f}")
    else:
        print("Invalid input. Please enter a positive number.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
