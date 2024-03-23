
# 5.17. Write a program to calculate the series: 5.6.7 + 6.7.8 + 7.8.9 + ... + n(n+1)(n+2)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n
for i in range(5, n + 1):
	seriesSum += i * (i + 1) * (i + 2)

print("Sum of the series:", seriesSum)