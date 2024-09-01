# 6.16.
# 		5 6 7 8 9
# 		4 5 6 7
# 		3 4 5
# 		2 3
# 		1

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(n, 0, -1):
	for c in range(1, r + 1):
		print(r + c - 1, end = " ")
	print()