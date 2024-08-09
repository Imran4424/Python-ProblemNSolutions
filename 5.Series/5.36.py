# 5.37. Write a program to print all number who is divible by y from n to 1 (y < n).

# Input the value of n
n = int(input("Enter the value of n: "))

# y
y = int(input("Enter the value of y: "))

for i in range(n, 0, -1):
    if i % y == 0:
        print(i)