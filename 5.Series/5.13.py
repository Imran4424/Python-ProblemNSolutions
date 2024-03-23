
# 5.13. Write a program to calculate the series: 1.1^2 + 2.3^2 + 3.5^2 + ... + n.(n + nth - 1)^2
# or
# 5.13. Write a program to calculate the series: 1.1^2 + 2.3^2 + 3.5^2 + ... + n.(n + 2)^2

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n
for i in range(1, n + 1):
	seriesSum += i * ((i + i - 1) ** 2)

print("Sum of the series:", seriesSum)