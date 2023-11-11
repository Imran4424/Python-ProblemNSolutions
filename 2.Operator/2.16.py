# 2.16. Write a program that read a number and mod by four using bitwise AND

num = int(input("Enter the int the number: "))

# modulus by n with AND - num & (n - 1)
modulusByFour = num & 3

print("Result after modulus by 4 is: ", modulusByFour)