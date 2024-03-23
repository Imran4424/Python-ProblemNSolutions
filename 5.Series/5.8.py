
# 5.8. Write a program to calculate the series: 1.3 + 3.5 + 5.7 + ... + n(n+2)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n
for i in range(1, n + 1, 2):
	seriesSum += i * (i + 2)

print("Sum of the series:", seriesSum)