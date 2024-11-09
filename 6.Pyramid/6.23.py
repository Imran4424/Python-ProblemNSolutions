# 6.23
#
#               1
#             0 0
#           1 1 1 
#         0 0 0 0 
#       1 1 1 1 1

# input the value of n
n = int(input("enter the value of n: "))

# build the pyramid
# first loop for row
for row in range(1, n + 1):
	# now put spaces at front
	for space in range(1, n - row + 1):
		print(" ", end = " ")

	# now put the values in each column
	for col in range(1, row + 1):
		if row % 2 == 0:
			print(0, end = " ")
		else:
			print(1, end = " ")

	# for a new line
	print()