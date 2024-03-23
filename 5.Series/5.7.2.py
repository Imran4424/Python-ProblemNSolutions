
# 5.7. Write a program to calculate the series: 2.1 + 5.3 + 8.5 + ... + n(n - nth)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 2, end value is n, increment by 3
count = 1 # to calculate the number of values in series

# althoug second range will not run till n + 1
# this loop is solely depend on first range
for i, j in zip(range(2, n + 1, 3), range(1, n + 1, 2)):
	seriesSum += i * j

print("Sum of the series:", seriesSum)