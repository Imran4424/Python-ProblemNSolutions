# 4.7. Write a program that read three numbers and display median

# Read three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# variable declaration with none
# this is the generic way to declare variable without a value
# later we can use any type of value inside this median
# in this case, we will use median as float type variabe later
median = None  

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

