# 1.24. Write a program that read any date in the format DD/MM/YYYY
# and displays day, month and year separately

import datetime

dateString = input("enter current date in this format, DD/MM/YYYY: ")

currentDate = datetime.datetime.strptime(dateString, "%d/%m/%Y")

print("Current day: ", currentDate.day)
print("Current Month: ", currentDate.month)
print("Current Year: ", currentDate.year)