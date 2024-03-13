
# 4.7. Write a program that read three numbers and display median

x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
z = float(input("enter the third number: "))

if (x > y and x < z) or (x > z and x < y):
    print("median is: ", x)
elif (y > z and y < x) or (y > x and y < z):
    print("median is: ", y)
elif (z > x and z < y) or (z > y and z < x):
    print("median is: ", z)


# Binary operators
# Logical operators

# and - logical and -  x and y - True only if both the operands are True
# or - logical or -  x or y - True if at least one of the operands is True
# not - logical not -  not x - True if the operand is False and vice-versa.

# Python special operators

# Identity Operators

# is - True if the operands are identical (refer to the same object) - x is True
# is not - True if the operands are not identical (do not refer to the same object) - x is not True



# Membership operators

# in - True if value/variable is found in the sequence - 5 in x
# not in - True if value/variable is not found in the sequence - 5 not in x