
# 5.9. Write a program to calculate the series: 1^2 + 2^2 + 3^2 + ... + n^2

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n
# value is not passed for increment
# if value not passed then increment will be by 1
for i in range(1, n + 1):
	seriesSum += i ** 2

print("Sum of the series:", seriesSum)