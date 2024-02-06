# 4.12. Write a program to input any character and check whether it is alphabet, digit or special character

digits = "0123456789"

character = input("enter the character: ")

# check whether it is single character or not
if len(character) == 1:
    if character.isalpha():
        print("Letter")
    elif character in digits:
        print("Digit")
    else:
        print("Special character")
else:
    print("Please enter a single letter")

