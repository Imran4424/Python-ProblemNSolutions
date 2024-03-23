
# 5.2. Write a program to calculate the series: 2 + 4 + 6 + 8 + ... + n

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 2, end value is n, increment by 2
for value in range(2, n + 1, 2):
	seriesSum += value

print("Sum of the series:", seriesSum)