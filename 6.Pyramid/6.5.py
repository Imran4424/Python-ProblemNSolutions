# 6.5.
# 		2
# 		3 4
# 		4 5 6
# 		5 6 7 8
# 		6 7 8 9 10

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(1, n + 1):
	for c in range(1, r + 1):
		print(r + c, end = " ")
	print()