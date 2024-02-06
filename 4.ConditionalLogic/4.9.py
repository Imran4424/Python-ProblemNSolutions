# 4.9. Write a program that read mark and display result in grade

marks = float(input("Enter the mark: "))

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 65:
    print("A-")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
elif marks >= 33:
    print("E")
else:
    print("F")
        