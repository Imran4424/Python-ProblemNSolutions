# 4.1. Write a program that read an integer and prints odd or even

# Get input from the user
numberInput = input("Enter an integer: ")

# Convert the input to an integer
try:
    enteredNumber = int(numberInput)

    # Check if the number is odd or even
    if enteredNumber % 2 == 0:
        print(f"{enteredNumber} is an even number.")
    else:
        print(f"{enteredNumber} is an odd number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")



# Binary Operator
# Compartion Operator

# == : equal operator ( 5 == 5 gives true, 3 == 5 gives false)
# != : Not Equal To ( 5 != 5 gives false, 3 != 5 gives true)
# > : Greater Than ( 5 > 3 gives true, 3 > 5 gives false)
# < : Less Than ( 5 < 3 gives false, 3 < 5 gives true)
# >= : Greater Than or Equal To ( 5 < 3 gives false, 3 < 5 gives true)