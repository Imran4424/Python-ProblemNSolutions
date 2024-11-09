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
# first loop for row
for row in range(1, n * 2):
	if row <= n:
		for col in range(1, row + 1):
			print(row, end = " ")
	else:
		for col in range(n * 2 - row):
			print(n * 2 - row, end = " ")

	print()