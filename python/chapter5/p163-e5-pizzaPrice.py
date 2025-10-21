# Redo Chapter 3 Exercise 2 with functions

import math

def circleArea(radius):
    return math.pi * radius ** 2

def costPerArea(dollars, squareInches):
    return dollars / squareInches

def main():
    diameter = float(input("Enter pizza diameter in inches: "))
    dollars = float(input("Enter total dollars: "))
    areaSqrIn = circleArea(diameter / 2)
    dollarsPerSqrIn = costPerArea(dollars, areaSqrIn)
    print("Price per square inch: $", round(dollarsPerSqrIn, 2), sep="")

main()