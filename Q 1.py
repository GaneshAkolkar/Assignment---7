month = int
(input("Enter a month number (1-12): "))

if month == 2:
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                days = 29
            else:
                days = 28
        else:
            days = 29
    else:
        days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 31

print("Number of days in month", month, "is", days)
