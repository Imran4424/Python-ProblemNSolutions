# 6.33.
# 			1
# 		      1 2 1
# 		    1 2 3 2 1
# 		  1 2 3 4 3 2 1
# 		1 2 3 4 5 4 3 2 1
# 		  1 2 3 4 3 2 1
# 		    1 2 3 2 1
# 		      1 2 1
# 			1

# input the value of n
n = int(input("enter the value of n: "))

# build the first part of the pyramid
# first loop for row
for row in range(1, n + 1):
	# now put spaces at front
	for space in range(1, n - row + 1):
		print(" ", end = " ")

	for col in range(1, row + 1):
		print(col, end = " ")

	for col in range(row - 1, 0, -1):
		print(col, end = " ")

	# for a new line
	print()

# build the second part of the pyramid
# first loop for row
for row in range(n - 1, 0, -1):
	# now put spaces at front
	for space in range(1, n - row + 1):
		print(" ", end = " ")

	for col in range(1, row + 1):
		print(col, end = " ")

	for col in range(row - 1, 0, -1):
		print(col, end = " ")

	# for a new line
	print()