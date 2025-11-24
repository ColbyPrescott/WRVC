# Write a program to turn month, day and year into a day of the year (and validate the date)
# a) dayNum = 31(month - 1) + day
# b) if the month is after februaru subtract (4(month) + 23) // 10
# c) if it's a leap year and after Febryary 29, add 1

def getLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def getValidDate(day, month, year):
    if month < 1 or month > 12:
        return False
    
    if day < 0 or month < 0:
        return False
    
    if day == 0:
        return False
    
    if day > 31:
        return False
    
    if month == 2 and day == 29 and not getLeapYear(year):
        return False
    
    if month == 2 and day > 29:
        return False

    thirtyMonths = [3, 5, 8, 10]
    if month != 2 and month in thirtyMonths and day > 30:
        return False
    
    if year < 0:
        return False
    
    return True

def main():
    print("This program will calculate day of the year from a date.")
    print()

    month = int(input("Enter month number (1-12): "))
    day = int(input("Enter day of month: "))
    year = int(input("Enter year: "))

    if not getValidDate(day, month, year):
        print("Date is not valid!")
        return
    
    dayNum = 31 * (month - 1) + day
    if month > 2:
        dayNum -= (4 * month + 23) // 10
    if getLeapYear(year) and month > 2:
        dayNum += 1
    
    print("Day of the year:", dayNum)

if __name__ == "__main__":
    main()