
# 5.7. Write a program to calculate the series: 2.1 + 5.3 + 8.5 + ... + n(n - nth)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 2, end value is n, increment by 3
count = 1 # to calculate the number of values in series

for value in range(2, n + 1, 3):
	seriesSum += value * (value - count)
	count += 1

print("Sum of the series:", seriesSum)