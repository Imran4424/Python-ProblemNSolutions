# 7.4. Write a program that read a positive integer and display its factorial

n = int(input("enter a positive integer for finding factorial: "))

# 1 as for indentity law
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    
print("Factorial of entered number is: ", factorial)

# 5! = 5 * 4 * 3 * 2 * 1

# but in this code we done 1 * 2 * 3 * 4 * 5
# the result is same