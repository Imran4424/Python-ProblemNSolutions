# 3.14. Write a program that read two numbers base, power and display the value of base^power

# Get input from the user
base_input = input("Enter the base: ")
power_input = input("Enter the power: ")

# Convert the inputs to floats
try:
    base = float(base_input)
    power = float(power_input)

    # Calculate and display the result using pow()
    result = pow(base, power)
    print(f"The result of {base} raised to the power of {power} is: {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers for both base and power.")
