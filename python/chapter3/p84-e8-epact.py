# Gregorian epact is number of days between January 1st and the previous new moon
# C = year//100
# epact = (8 + (C//4) - C + ((8C + 13)//25) + 11(year%19))%30
# Prompt the user for a four-digit year and then output the epact

def main():
    year = int(input("Enter a four-digit year: "))
    
    C = year // 100
    epact = (8 + (C // 4) - C + ((8*C + 13) // 25) + 11*(year % 19)) % 30
    
    print("The epact is:", epact)

main()