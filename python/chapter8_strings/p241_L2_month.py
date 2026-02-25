# A program to print the abbreviation of a month, given its number

def main():
    # months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1-12): "))

    # Computer starting position of month n nin months
    pos = (n - 1) * 3

    # Grab the appropriate slice from months
    month_abbrev = months[pos:pos+3]

    # Print the result
    print("The month abbreviation is", month_abbrev + ".")

if __name__ == "__main__":
    main()