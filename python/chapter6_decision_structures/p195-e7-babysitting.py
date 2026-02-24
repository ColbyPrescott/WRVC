# Write a program to calculate the babysitting bill
# Input a starting and ending time, hour and minute of a 24 hour format
# $12.50 per hour until 9:00 PM when the rate drops to $11.50 and hour
# Assuming it's back to $12.50 per hour at midnight

def main():
    print("Babysitting from aa:bb to cc:dd in a 24 hour format")
    startHour = int(input("Enter hour of start time: "))
    startHour += int(input("Enter minute of start time: ")) / 60
    endHour = int(input("Enter hour of ending time: "))
    endHour += int(input("Enter minute of end time: ")) / 60

    # If babysitting through midnight, bump end time to the next day
    if endHour < startHour:
        endHour += 24

    # Constant markers
    sleepHour = 21
    midnightHour = 24

    # Running totals
    normalHours = 0
    sleepHours = 0
    # Temporary marker
    currentHour = startHour

    # Step thorugh each section of the day
    while currentHour < endHour:
        if currentHour % 24 < sleepHour:
            # Time from currentHour to endHour or the next sleep marker
            hours = min(endHour, currentHour // 24 * 24 + sleepHour) - currentHour
            normalHours += hours
            currentHour += hours
        else:
            # Time from currentHour to endHour or the next midnight marker
            hours = min(endHour, currentHour // 24 * 24 + midnightHour) - currentHour
            sleepHours += hours
            currentHour += hours
    
    finalDollars = 12.50 * normalHours + 11.50 * sleepHours
    print("Final pay: $", finalDollars, sep="")

if __name__ == "__main__":
    main()