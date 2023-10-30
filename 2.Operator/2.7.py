# 2.7. Write a program that read radius of a circle and display the area

PI = 3.1416

radius = float(input("enter the radius of the circle: "))

area = PI * radius ** 2

print("Area is: ", area)


# square can be written in 3 ways

# ** - number ** exponent
# pow(base, exponent)
# math.pow(number, exponent)