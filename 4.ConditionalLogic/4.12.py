# 4.12. Write a program to input any character and check whether it is alphabet, digit or special character

# declaring a string of all digits
digits = "0123456789"

character = input("enter the character: ")

# check whether it is single character or not
if len(character) == 1:
    # checking if the character letter or not
    if character.isalpha():
        print("Letter")
    # checking if the digits in the string or not
    elif character in digits:
        print("Digit")
    else:
        print("Special character")
else:
    print("Please enter a single letter")

