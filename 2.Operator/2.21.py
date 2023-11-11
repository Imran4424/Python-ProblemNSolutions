# 2.21. Write a program that read two numbers and display minimum using ternary operator

numOne = int(input("Enter the first the number: "))
numTwo = int(input("Enter the second the number: "))

minVal = numOne if (numOne < numTwo) else numTwo

print("Min value is: ", minVal)