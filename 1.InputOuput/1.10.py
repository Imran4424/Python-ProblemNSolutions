# 1.10. Write a program that read any upper case character and
# display in lower case

character = input("Enter a uppercase character: ")

while character[0] < "A" or character > "Z":
    print("Wrong input")
    character = input("Enter a lowercase character: ")

print("Lowercase character of entered character is: ", chr(ord(character[0]) + 32))