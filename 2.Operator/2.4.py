# 2.4. Write a program that read two integers and divide them

x = int(input("enter the first int number: "))
y = int(input("enter the second int number: "))

while y == 0:
    print("second integer is zero")
    y = int(input("enter the second int number: "))

# in c, if we divide two integers, result will be also integer
# but in python even two integers dividation result in floating value
print("Result is: ", x / y)