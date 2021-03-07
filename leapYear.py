def leapYear(year):
    if year % 4 != 0:
        print(year, ' is not a leap year')
        return str(year) + ' is not a leap year'
    
    elif year % 100 == 0:
        print(year, ' is not a leap year')
        return str(year) + ' is not a leap year'