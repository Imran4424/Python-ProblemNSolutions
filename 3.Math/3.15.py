# 3.15. Write a program that read any number and display it's square root

import math

# Get input from the user
number_input = input("Enter a number: ")

# Convert the input to a float
try:
    number = float(number_input)

    # Check if the number is non-negative before calculating the square root
    if number >= 0:
        # Calculate and display the square root
        square_root = math.sqrt(number)
        print(f"The square root of {number} is: {square_root:.4f}")
    else:
        print("Invalid input. Please enter a non-negative number.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
