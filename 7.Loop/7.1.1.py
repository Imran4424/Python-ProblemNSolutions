# 7.1. Write down a program that can take a lower bound i and an upper bound n and then find out the summation of
#    those numbers which are even from i to n.

i = int(input("enter the lower bound: "))
n = int(input("enter the upper bound: "))

sum = 0

x = i

while x <= n:
    if x % 2 == 0:
        sum = sum + x
    x = x + 1

print("Summation of even numbers from", i, " to", n, " is: ", sum)
