# 4.3. Write a program that read two numbers and display maximum

# Get input from the user for the first number
number1Input = input("Enter the first number: ")

# Get input from the user for the second number
number2Input = input("Enter the second number: ")

# Convert the inputs to floats
try:
    num1 = float(number1Input)
    num2 = float(number2Input)

    # Find and display the maximum of the two numbers
    maximum = max(num1, num2)
    print(f"The maximum of {num1} and {num2} is: {maximum}")

except ValueError:
    print("Invalid input. Please enter valid numbers for both numbers.")
