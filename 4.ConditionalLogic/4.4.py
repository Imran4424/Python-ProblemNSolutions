# 4.4. Write a program that read two numbers and display minimum

# Get input from the user for the first number
number1Input = input("Enter the first number: ")

# Get input from the user for the second number
number2Input = input("Enter the second number: ")

# Convert the inputs to floats
try:
    num1 = float(number1Input)
    num2 = float(number2Input)

    # Find and display the minimum of the two numbers
    minimum = min(num1, num2)
    print(f"The minimum of {num1} and {num2} is: {minimum}")

except ValueError:
    print("Invalid input. Please enter valid numbers for both numbers.")
