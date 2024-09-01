# 6.9.
# 		A
# 		B B
# 		C C C
# 		D D D D 
# 		E E E E E

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(1, n + 1):
	for c in range(1, r + 1):
		print(chr(ord('A') + r - 1), end = " ")
	print()





# here
# ord() to obtain ASCII value from character
# chr() to obtain character from ASCII value