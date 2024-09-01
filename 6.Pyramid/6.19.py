# 6.19.
# 		E E E E E
# 		D D D D
# 		C C C
# 		B B
# 		A

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(n, 0, -1):
	for c in range(1, r + 1):
		print(chr(ord('A') + r - 1), end = " ")
	print()





# here
# ord() to obtain ASCII value from character
# chr() to obtain character from ASCII value