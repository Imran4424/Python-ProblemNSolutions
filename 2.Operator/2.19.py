# 2.19. Write a program to swap the values of two variables without using temporary variable

numOne = int(input("Enter the first the number: "))
numTwo = int(input("Enter the second the number: "))

numOne = numOne + numTwo
numTwo = numOne - numTwo
numOne = numOne - numTwo

print("After swap numOne is: ", numOne)
print("After swap numTwo is: ", numTwo)
