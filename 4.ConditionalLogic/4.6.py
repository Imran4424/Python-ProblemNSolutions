# 4.6. Write a program that read three numbers and display minimum

# Get input from the user for the first number
number1Input = input("Enter the first number: ")

# Get input from the user for the second number
number2Input = input("Enter the second number: ")

# Get input from the user for the third number
number3Input = input("Enter the third number: ")

# Convert the inputs to floats
try:
    num1 = float(number1Input)
    num2 = float(number2Input)
    num3 = float(number3Input)

    # Find and display the minimum of the three numbers
    minimum = min(num1, num2, num3)
    print(f"The minimum of {num1}, {num2}, and {num3} is: {minimum}")

except ValueError:
    print("Invalid input. Please enter valid numbers for all three numbers.")
