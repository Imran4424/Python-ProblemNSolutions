
# 5.16. Write a program to calculate the series: 2.5.8 + 5.8.11 + 8.11.14 + ... + n(n+3)(n+6)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n
for i in range(2, n + 1, 3):
	seriesSum += i * (i + 3) * (i + 6)

print("Sum of the series:", seriesSum)