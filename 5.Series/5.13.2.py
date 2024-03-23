
# 5.13. Write a program to calculate the series: 1.1^2 + 2.3^2 + 3.5^2 + ... + n.(n + nth - 1)^2
# or
# 5.13. Write a program to calculate the series: 1.1^2 + 2.3^2 + 3.5^2 + ... + n.(n + 2)^2

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n

# second loop end value in n + 2, terminating point is n + 3
# because problem is design to depend on first loop
# so making sure second loop doesn't stop earlier than first loop
for i, j in zip(range(1, n + 1, 1), range(1, n + 3, 2)):
	seriesSum += i * (j ** 2)

print("Sum of the series:", seriesSum)