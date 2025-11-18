# Write a program that calculates if a given year is a leap year or not
# Must be divisible by 4, unless it is a century year that is not divisible by 400. (1800 and 1900 are not leap years while 1600 and 2000 are leap years)

def main():
    print("Calculates if a year is a leap year or not")
    print()

    year = int(input("Enter a year: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

if __name__ == "__main__":
    main()