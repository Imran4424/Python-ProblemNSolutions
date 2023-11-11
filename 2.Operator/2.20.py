# 2.20. Write a program that read two numbers and display maximum using ternary operator

numOne = int(input("Enter the first the number: "))
numTwo = int(input("Enter the second the number: "))

maxVal = numOne if (numOne > numTwo) else numTwo

print("Max value is: ", maxVal)