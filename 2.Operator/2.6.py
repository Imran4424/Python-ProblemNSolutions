# 2.6. Write a program that read two integer and display remainder

x = int(input("enter the first int number: "))
y = int(input("enter the second int number: "))

while y == 0:
    print("second integer is zero")
    y = int(input("enter the second int number: "))

print("Remainder is: ", x % y)