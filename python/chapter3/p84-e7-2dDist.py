# Calculate distance between two points

import math

def main():
    print("Calculate distance between (x1, y1) and (x2, y2)")
    
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    print("Distance:", dist)

main()