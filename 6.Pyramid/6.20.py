# 6.20.
# 		A B C D E
# 		A B C D
# 		A B C
# 		A B
# 		A

# Input the value of n
n = int(input("Enter the value of n: "))

# build the pyramid
for r in range(n, 0, -1):
	for c in range(1, r + 1):
		print(chr(ord('A') + c - 1), end = " ")
	print()





# here
# ord() to obtain ASCII value from character
# chr() to obtain character from ASCII value