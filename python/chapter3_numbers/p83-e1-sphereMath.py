# Calculate volume and surface area of a sphere given its radius as an input
# V = 4/3pir^3
# A = 4pir^2

import math

def main():
    radius = float(input("Enter sphere radius: "))
    volume = (4 / 3) * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2
    
    print("Volume:", volume)
    print("Area:", area)

main()