
# 4.14. Write a program to generate a simple arithmetic calculator

# hints: 
# enter two numbers: 6 5
# select the menu:
#	1. Add
#	2. Subtract
#	3. Multiply
#	4. Divide

operations = [1, 2, 3, 4, 5]

print("Enter two numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select the operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = int(input("Enter choice (1/2/3/4/5): "))

if choice in operations:
    if choice == 1:
        print("Result is: ", num1 + num2)
    elif choice == 2:
        print("Result is: ", num1 - num2)
    elif choice == 3:
        print("Result is: ", num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result is: ", num1 / num2)
    else:
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result is: ", num1 % num2)
            
else:
    print("Invalid input")