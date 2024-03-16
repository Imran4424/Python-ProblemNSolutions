
# 4.7. Write a program that read three numbers and display median

x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
z = float(input("enter the third number: "))


# finding middle value among three

# using nested if
if x > y:
    # x > y
    if x < z:
        # x > y and x < z
        print("Median is: ", x)
    else:
        # x > y and x > z
        if y > z:
            # x > y and x > z and y > z
            print("Median is:", y)
        else:
            # x > y and x > z and y > z
            print("Median is:", z)
        
elif y > z:
    # y > z and y > x
    if z > x:
        # y > z and y > x and z > x
        print("Median is: ", z)
    else:
        # y > z and y > x and z < x
        print("Median is: ", x)
elif z > x:
    # z > x and y < z and x < y
    print("Median is: ", y)
    
        
    
    

