# 4.11. Write the code to check whether an input alphabet is a vowel or not.
# Both lower-case and upper-case should be checked

vowels = "aeiouAEIOU"

letter = input("enter the letter: ")

# Check if the input letter is a vowel and display the result
if len(letter) == 1 and letter.isalpha():
    if letter in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single letter")
    

# letter.isalpha() validates entered character is alphabet or not