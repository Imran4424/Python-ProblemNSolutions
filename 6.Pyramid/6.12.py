# 6.12.
# 		5 5 5 5 5
# 		4 4 4 4
# 		3 3 3
# 		2 2
# 		1

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(n, 0, -1):
	for c in range(1, r + 1):
		print(r, end = " ")
	print()