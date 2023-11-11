# 2.13. Write a program that read a number and divide by two using shift operator

num = int(input("Enter the int the number: "))

# just right shift once
divideByTwo = num >> 1

print("Result after divide by 2 is: ", divideByTwo)