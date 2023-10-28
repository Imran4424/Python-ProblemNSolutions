# 1.17. Write a program that read as many characters as need to read your name and
# display the characters sequencially with spaces

name = input("enter your name: ")

for letter in name:
    print(letter, end = " ") # end is the end character of print method
    # by default end holds "\n" which is new line (default parameter)
    # we can change it by passing it manually
    # it this case we are passing space
    
    
    
    
    
# print sytax
# print(object(s), sep=separator, end=end, file=file, flush=flush)

# object(s) - Any object, and as many as you like. Will be converted to string before printed

# sep='separator' - Optional. Specify how to separate the objects, if there is more than one. Default is " "(space)

# end='end' - Optional. Specify what to print at the end. Default is "\n" (line feed)

# file - Optional. An object with a write method. Default is sys.stdout

# flush - Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False