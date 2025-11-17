# Write a program that calculates the date of Easter for the years 1982 - 2048 inclusive
# let a = year%19, b = year%4, c = year%7, d = (19a+24)%30, e = (2b+4c+6d+5)%7.
# Date of Easter is March 22 + d + e (which could be in April)
# This formula also works for every year within 1900-2099 except for 
#   1954, 1981, 2049, and 2076, which are predicted 1 week late

def main():
    year = int(input("Enter year from 1900 through 2099 to calculate the date of Easter: "))

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7

    day = 22 + d + e
    month = "March"

    lateYears = [1954, 1981, 2049, 2076]
    if year in lateYears:
        day -= 7

    if day > 31:
        day -= 31
        month = "April"
    
    print("Easter is on ", month, " ", day, ", " , year, sep="")

if __name__ == "__main__":
    main()