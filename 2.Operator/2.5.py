# 2.5. Write a program that read two floating point numbers and divide them

x = float(input("enter the first float number: "))
y = float(input("enter the second float number: "))

while y == 0.0:
    print("second integer is zero")
    y = float(input("enter the second int number: "))

# in c, if we divide two integers, result will be also integer
# but in python even two integers dividation result in floating value
print("Result is: ", x / y)