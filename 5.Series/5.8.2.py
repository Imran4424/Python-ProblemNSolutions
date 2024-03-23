
# 5.8. Write a program to calculate the series: 1.3 + 3.5 + 5.7 + ... + n(n+2)

# Input the value of n
n = int(input("Enter the value of n: "))

seriesSum = 0

# range gives your range of 
# start value to end - 1 value
# start from 1, end value is n

# second loop end value in n + 2, terminating point is n + 3
# because problem is design to depend on first loop
# so making sure second loop doesn't stop earlier than first loop
for i, j in zip(range(1, n + 1, 2), range(3, n + 3, 2)):
	seriesSum += i * j

print("Sum of the series:", seriesSum)