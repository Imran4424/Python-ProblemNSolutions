# 7.5. Write a program that read a positive integer and display sum of its digit

number = int(input("enter a positive integer number: "))

# we are putting 0 for initialization by identity law
digitSum = 0

while number / 10 != 0:
    digit = number % 10
    digitSum = digitSum + digit
    
    # now for discarding last digit
    # it will not return interger, although number is already integer
    # number = number / 10
    # for getting the integer value, you need to typecast it after dividation
    number = int(number / 10)
    #print(number)
    
print("Digit sum of given number is: ", digitSum)

# say given number is 132
# sum of it's digit wil be 1 + 3 + 2 = 6

# to extract a digit, modulus the number by 10
# 132 % 10 = 2
# then divide it by 10, 132 / 10 = 13
# then, 13 % 10 = 3
# then again, 13 / 10 = 1
# then, 1 % 10 = 1
# then again, 1 / 10 = 0, when you get 0 just stop the operation

# 2 + 3 + 1 = 6
# sum is happening in reverse order
# because when we extract a digit by 10, we always extract the last digit