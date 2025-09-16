# Calculate area of triangle given the length of its three sides
# s = (a + b + c) / 2
# A = sqrt(s(s - a)(s - b)(s - c))

import math

def main():
    print("Calculate the area of a triangle given side lengths a, b, and c.")
    
    a = float(input("Enter side length a: "))
    b = float(input("Enter side length b: "))
    c = float(input("Enter side length c: "))
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print("Area:", area)

main()