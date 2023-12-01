# 3.1. Write a program that read any integer number and display absolute value

# Get input from the user
user_input = input("Enter an integer: ")

# Convert the input to an integer
try:
    number = int(user_input)
    # Calculate and display the absolute value
    absolute_value = abs(number)
    print(f"The absolute value of {number} is {absolute_value}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
