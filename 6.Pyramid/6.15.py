# 6.15.
# 		6 7 8 9 10
# 		5 6 7 8
# 		4 5 6
# 		3 4
# 		2

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(n, 0, -1):
	for c in range(1, r + 1):
		print(r + c, end = " ")
	print()