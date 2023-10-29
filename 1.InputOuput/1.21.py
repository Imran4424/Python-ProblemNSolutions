# 1.21. Write a program that read any date and displays in the format DD-MM-YYYY

import datetime

# get the current date and time
# dd-mm-YY
currentDate = datetime.date.today()

print(currentDate)

# dd-mm-YY H:M:S format
currentDateTime = datetime.datetime.now()

print(currentDateTime)