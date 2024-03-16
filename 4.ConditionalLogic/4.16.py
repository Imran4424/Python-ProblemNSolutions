
# 4.16. Write a program to input angles of a triangle and check whether triangle is valid or not

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180.0:
    print("Triangle is valid")
else:
    print("Triangle is not valid")