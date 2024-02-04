# 4.2. Write a program to determine whether a number is divisible by 5 or not

# Get input from the user
numberInput = input("Enter an integer: ")

# Convert the input to an integer
try:
    enteredNumber = int(numberInput)

    # Check if the number is odd or even
    if enteredNumber % 5 == 0:
        print(f"{enteredNumber} is divisible by five.")
    else:
        print(f"{enteredNumber} is not divisible by five.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")