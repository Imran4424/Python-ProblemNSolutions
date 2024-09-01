# 6.17.
# 		0 1 0 1 0
# 		1 0 1 0
# 		0 1 0
# 		1 0
# 		0

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(n, 0, -1):
	for c in range(1, r + 1):
		print(0 if (r + c) % 2 == 0 else 1, end = " ")
	print()