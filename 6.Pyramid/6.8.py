# 6.8.
# 		1
# 		0 1
# 		1 0 1
# 		0 1 0 1
# 		1 0 1 0 1

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(1, n + 1):
	for c in range(1, r + 1):
		print(1 if (r + c) % 2 == 0 else 0, end = " ")
	print()