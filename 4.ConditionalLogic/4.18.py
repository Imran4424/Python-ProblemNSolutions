
# 4.18. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

# Input lengths of the sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("\nThe triangle is valid\n")
    
    # Check if all sides are equal
    if side1 == side2 == side3:
        print("Equilateral Triangle")
    # Check if at least two sides are equal
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles Triangle")
    else:
        # If no sides are equal
        print("Scalene Triangle")
else:
    print("The triangle is not valid")