# 6.31.
# 			1
# 		      2 2
# 		    3 3 3
# 		  4 4 4 4
# 		5 5 5 5 5
# 		  4 4 4 4
# 		    3 3 3
# 		      2 2
# 			1

# input the value of n
n = int(input("enter the value of n: "))

# build the pyramid
# first loop for row
for row in range(1, n * 2):
	if row <= n:
		# now put spaces at front
		for space in range(1, n - row + 1):
			print(" ", end = " ")

		for col in range(1, row + 1):
			print(row, end = " ")
	else:
		# now put spaces at front
		for space in range(row - n):
			print(" ", end = " ")

		for col in range(n * 2 - row):
			print(n * 2 - row, end = " ")

	# for a new line
	print()