# Podunksville charges a speeding ticket with a flat $50, plus $5 for each mph over, plus another $200 for any speed over 90 mph.
# Write program that takes speed limit and clocked speed and calculates fine and if speed was legal

def main():
    speedLimitMPH = float(input("Enter speed limit (mph): "))
    clockedSpeedMPH = float(input("Clocked speed (mph): "))

    if clockedSpeedMPH <= speedLimitMPH:
        print("You're good σωσ")
        return

    fineDollars = 50
    fineDollars += 5 * (clockedSpeedMPH - speedLimitMPH)
    if clockedSpeedMPH > 90:
        fineDollars += 200
    
    print("Oooohh no you've been a bad little creature. Here's a $", fineDollars, " fine!", sep="")

main()