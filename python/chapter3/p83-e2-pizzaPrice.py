# Calculate cost per square inch of circular pizza given diameter and price
# A = pir^2

import math

def main():
    diameter = float(input("Enter pizza diameter in inches: "))
    dollarsPerSqrInch = float(input("Enter dollars per square inch: "))
    area = math.pi * (diameter / 2) ** 2
    cost = area * dollarsPerSqrInch
    print("Final price: $", round(cost, 2), sep="")

main()