
# 5.4. Write a program to calculate the series: 4 + 12 + 20 + 28 + ... + n

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 4, end value is n, increment by 8
for value in range(4, n + 1, 8):
	seriesSum += value

print("Sum of the series:", seriesSum)