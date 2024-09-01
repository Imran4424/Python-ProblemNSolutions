# 6.6.
# 		1
# 		2 3
# 		3 4 5
# 		4 5 6 7
# 		5 6 7 8 9

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(1, n + 1):
	for c in range(1, r + 1):
		print(r + c - 1, end = " ")
	print()