# 7.3. Write a program to print multiplication table of any number

n = int(input("enter the desired number to find out the table: "))

for i in range(1, 11):
    print(n, " x ", i, " = ", i * n)