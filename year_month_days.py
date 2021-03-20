def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    if isYearLeap(year) and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

print(daysInMonth(2000, 2))

def dayOfYear(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day > 31 or day < 0:
        return None
    days = 0
    for m in range(month):
        days += daysInMonth(year, m + 1)
    return days

print(dayOfYear(2001, 12, 32))