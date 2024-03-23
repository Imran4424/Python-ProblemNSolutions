
# 5.3. Write a program to calculate the series: 1 + 3 + 5 + 7 + ... + n

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n, increment by 2
for value in range(1, n + 1, 2):
	seriesSum += value

print("Sum of the series:", seriesSum)