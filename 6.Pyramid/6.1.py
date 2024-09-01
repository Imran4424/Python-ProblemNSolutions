# 6.1.    
# 		1
# 		1 2
# 		1 2 3
# 		1 2 3 4
# 		1 2 3 4 5

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(1, n + 1):
	for c in range(1, r + 1):
		print(c, end = " ")
	print()