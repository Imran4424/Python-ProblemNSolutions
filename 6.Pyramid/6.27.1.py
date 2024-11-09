# 6.27.
# 		A
# 		B B
# 		C C C
# 		D D D D 
# 		E E E E E
# 		D D D D 
# 		C C C
# 		B B
#		A

# input the value of n
n = int(input("enter the value of n: "))

# build the pyramid

# build first part of the pyramid
# first loop for row
for row in range(1, n + 1):
	for col in range(1, row + 1):
		print(chr(ord("A") + row - 1), end = " ")
	print()

# build second part of the pyramid
for row in range(n - 1, 0, -1):
	for col in range(1, row + 1):
		print(chr(ord("A") + row - 1), end = " ")
	print()