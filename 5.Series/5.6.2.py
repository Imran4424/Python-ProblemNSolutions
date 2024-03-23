
# 5.6. Write a program to calculate the series: 1.2 + 2.3 + 3.4 + ... + n(n+1)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
for i, j in zip(range(1, n + 1), range(2, n + 1)):
	seriesSum += i * j

print("Sum of the series:", seriesSum)