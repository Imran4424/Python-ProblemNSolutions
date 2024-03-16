
# 4.15. Write a program that read three numbers a, b, c and determine the roots of the quadratic equation:
#			ax^2 + bx + c = 0

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = (b ** 2) - 4 * a * c

print("Roots of the quadratic equation are: ")

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("root 1: ", root1)
    print("root 2: ", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("root 1: ", root)
    print("root 2: ", root)
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(abs(discriminant)) / (2 * a)
    print("root 1: ", (realPart, imaginaryPart))
    print("root 2: ", (realPart, -imaginaryPart))
# equation

# root1 = (- b + sqrt(b^2 - 4ac)) / 2 * a
# root2 = (- b - sqrt(b^2 - 4ac)) / 2 * a