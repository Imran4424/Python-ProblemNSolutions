# 2.15. Write a program that read a number and multiply by five using shift operator

num = int(input("Enter the int the number: "))

# just left shift twice + num
multiplyByFive = (num << 2) + num

print("Result after multiply by 5 is: ", multiplyByFive)