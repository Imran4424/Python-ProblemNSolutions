# 2.18. Write a program to swap the values of two variables using temporary variable

numOne = int(input("Enter the first the number: "))
numTwo = int(input("Enter the second the number: "))

temp = numOne
numOne = numTwo
numTwo = temp

print("After swap numOne is: ", numOne)
print("After swap numTwo is: ", numTwo)