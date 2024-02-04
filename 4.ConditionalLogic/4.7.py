# 4.7. Write a program that read three numbers and display median

# Read three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

median = 5.0 # initial value just to declare float type variable

# calculate the median 
if num1 >= num2:
	if num2 >= num3:
		median = num2
	elif num1 <= num3:
		median = num1
	else:
		median = num3
elif num1 > num3:
	median = num1
elif num2 > num3:
	median = num3
else:
	median = num2

# display the median
print("The median is: ", median)
