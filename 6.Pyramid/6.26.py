# 6.26
#
#               A
#              B B
#             C C C
#            D D D D
#           E E E E E

# input the value of n
n = int(input("enter the value of n: "))

# build the pyramid
# first loop for row
for row in range(1, n + 1):
	# now put spaces at front
	for space in range(1, n - row + 1):
		# no space after the space
		print(" ", end = "")

	# now put the values in each column
	for col in range(1, row + 1):
		print(chr(ord("A") + row - 1), end = " ")

	# for a new line
	print()