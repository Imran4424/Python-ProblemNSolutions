# 5.36. Write a program to print all number who is divible by 5 from n to 1.

# Input the value of n
n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    if i % 5 == 0:
        print(i)