# 6.30.
# 		1
# 		2 2
# 		3 3 3
# 		4 4 4 4
# 		5 5 5 5 5
# 		4 4 4 4 
# 		3 3 3
# 		2 2
#		1

# input the value of n
n = int(input("enter the value of n: "))

# build the pyramid

# build first part of the pyramid
# first loop for row
for row in range(1, n + 1):
	for col in range(1, row + 1):
		print(row, end = " ")
	print()

# build second part of the pyramid
for row in range(n - 1, 0, -1):
	for col in range(1, row + 1):
		print(row, end = " ")
	print()