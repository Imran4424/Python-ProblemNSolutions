# 2.22. Write a program that reads two numbers and display the maximum without using relational operators

def largeNumber(a, b):
    diff = a - b
    sign = (diff >> 31) & 1  # Assuming 32-bit integers

    # If sign is 0, 'a' is larger; if sign is 1, 'b' is larger
    larger_number = a - sign * diff

    return larger_number

numOne = int(input("enter a int number: "))
numTwo = int(input("enter a int number: "))


print("The large number is: ", largeNumber(numOne, numTwo))