# 1.22. Write a program that read any date and displays in the format DD MM YYYY

import datetime

# get the current date and time
now = datetime.datetime.now()

# dd mm YY
currentDate = now.strftime("%d %m %Y")

print(currentDate)

# dd mm YY H:M:S format
currentDateTime = now.strftime("%d %m %Y, %H:%M:%S")

print(currentDateTime)