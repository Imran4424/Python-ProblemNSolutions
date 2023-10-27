# 1.9. Write a program that read any lower case character and
# display in upper case

character = input("Enter a lowercase character: ")

while character[0] < "a" or character > "z":
    print("Wrong input")
    character = input("Enter a lowercase character: ")

print("Uppercase character of entered chracter is: ", chr(ord(character[0]) - 32))