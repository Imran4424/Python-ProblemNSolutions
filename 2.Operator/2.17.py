# 2.17. Write a program that read a number and mod by eight using bitwise AND

num = int(input("Enter the int the number: "))

# modulus by n with AND - num & (n - 1)
modulusByEight = num & 7

print("Result after modulus by 7 is: ", modulusByEight)