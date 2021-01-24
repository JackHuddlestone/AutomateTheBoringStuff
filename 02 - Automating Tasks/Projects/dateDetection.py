import re

# Regex to detect date.
dateDetection = re.compile(r'''(0?[1-9]|[1-3][0-9])\/(0?[1-9]|1[012])/([1-2][0-9][0-9][0-9])''')

# Error message is date is not valid.
def notValid():
    try:
        print(f'{str(day)}/{str(month)}/{str(year)} is not a valid date. Please try again.\n')
    except NameError:
        print(f'Invalid input - "{str(date)}" - Please try again.')

# Work out if the year is a leap year.
def isLeapYear(year):
    # Determines if the year is a leap year.
    if int(year) % 4 == 0:

        # If year is divisible by 100 but not divisible by 400, it is not a leap year.
        if int(year) % 100 == 0 and int(year) % 400 != 0:
            return False

        # If year is divisible by both 100 and 400.
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            return True

        # If the year is divisible by 4 then it is a leap year.
        else:
            return True

    else:
        return False
    
# Months with 30 days in them.
short_months = ['04', '06', '09', '11']

# Logic to see if date is valid.
validDate = False
while (validDate == False):
    # Input for user to find date.
    date = input('Please input a date. (DD/MM/YYYY) - Type "Q" to quit. ')
    if date == 'q'.lower():
        print('Quitting...')
        break

    while True:
        # Perform search and segregate date into groups.
        try:
            day = dateDetection.search(date).group(1)
            month = dateDetection.search(date).group(2)
            year = dateDetection.search(date).group(3)
        except (AttributeError, NameError):
            notValid()
            break
            
        # If more than 31 days in a month, the date is not valid.
        if int(day) > 31:
            notValid()
            break

        # If more than 30 days in a April, June, September or November the date is not valid.
        if int(day) > 30 and str(month) in short_months:
            notValid()
            break

        # If a leapyear and there is more than 29 days in February the date is not valid.
        if isLeapYear(year) == True:
            if str(month) == '02' and int(day) > 29:
                print(f'{str(day)} is not a valid date on a leap year in February.')
                notValid()
                break
            else:
                print(f'{str(day)}/{str(month)}/{str(year)} is a valid date, and is a leap year.')
                validDate = True
                break
        
        # If not a leapyear and there is more than 28 days in February the date is not valid.
        if isLeapYear(year) == False:
            if str(month) == '02' and int(day) > 28:
                print(f'{str(day)} is not a valid date in February which is not a leap year..')
                notValid()
                break

            else:
                print(f'{str(day)}/{str(month)}/{str(year)} is a valid date, and is a not a leap year.')
                validDate = True
                break

        




            



    

    