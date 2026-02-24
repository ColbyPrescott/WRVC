# Calculate length of ladder to reach height given angle
# length = height / sin(angle)
# Prompt for degrees, convert to radians
# radians = (pi / 180) degrees

import math

def main():
    print("Calculate the length of a ladder needed to reach a specific height (ft) at an angle (degrees).")
    
    heightFt = float(input("Enter desired height (ft): "))
    angleDeg = float(input("Enter desired angle (degrees):"))
    
    angleRad = (math.pi / 180) * angleDeg
    lengthFt = heightFt / math.sin(angleRad)
    
    print("Ladder length:", lengthFt, "ft")

main()