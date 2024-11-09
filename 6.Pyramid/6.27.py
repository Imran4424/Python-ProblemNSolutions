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
# first loop for row
for row in range(1, n * 2):
	if row <= n:
		for col in range(1, row + 1):
			print(chr(ord("A") + row - 1), end = " ")
	else:
		for col in range(n * 2 - row):
			print(chr(ord("A") + n * 2 - row - 1), end = " ")

	print()