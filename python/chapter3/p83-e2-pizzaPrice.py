# Calculate cost per square inch of circular pizza given diameter and price
# A = pir^2

import math

def main():
    diameter = float(input("Enter pizza diameter in inches: "))
    dollars = float(input("Enter total dollars: "))
    area = math.pi * (diameter / 2) ** 2
    dollarsPerSqrIn = dollars / area
    print("Price per square inch: $", round(dollarsPerSqrIn, 2), sep="")

main()