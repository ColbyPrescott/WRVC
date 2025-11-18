# Write a program that can take a day, month, and year numbers and calculate if it is a valid date or not
# Ex: 5/24/1962 is valid but 9/31/2000 is not because September only has 30 days

import time
import os

thirtyMonths = [3, 5, 8, 10]
monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "Septemper",
    "October",
    "November",
    "December"
]

# Would use an import statement to use p196-e11-leapYear.py but the import keyword doesn't like the hyphens
def getLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def main():
    print("This program determines if a date is valid or not")
    print()

    day = month = year = 0
    try:
        day = float(input("Enter the day: "))
        month = float(input("Enter the month #: "))
        year = float(input("Enter the year: "))
    except ValueError:
        print("Value is not a number!")
        return

    if round(day) != day or round(month) != month or round(year) != year:
        print("Please remove the decimal points, they are a little too crunchy for my liking")
        return
    
    day = int(day)
    month = int(month)
    year = int(year)

    if month < 1 or month > 12:
        print("Month is not in the range of 1 through 12")
        return
    
    if day < 0 or month < 0:
        print("Great Scott, you're a time traveler!!")
        print("Quick, abort access!")
        time.sleep(4)
        os.system("shutdown /s /t 0")
        return
    
    if day == 0:
        print("Each month starts at day 1, not day 0")
        return
    
    if day > 31:
        print("What are you trying? You know there's no months with more than 31 days, silly")
        return
    
    if month == 2 and day == 29 and not getLeapYear(year):
        print("Okay yes February has 29 days on a leap year, but", year, "is not a leap year!")
        return
    
    if month == 2 and day > 29:
        i = 0
        message = "It is coming. "
        while True:
            for j in range(int(1.01 ** i)):
                print(message, end="")
            print()
            time.sleep(max(0.01, 3 * (0.9 ** i)))
            i += 1

    if month != 2 and month in thirtyMonths and day > 30:
        print(monthNames[month - 1], "only has 30 days")
        return
    
    if year < 0:
        print("Okay Mr. Bones, I'll compute your", year)
    
    print(monthNames[month - 1], " ", day, ", ", year, " is a valid date!", sep="")

if __name__ == "__main__":
    main()