# We have not yet learned if statements, so this version uses a slightly less intuitive conversion of the algorithm with no branching

# Calculate an approximation for pi by summing a certain series, with the user inputting the number of terms
# Series: (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) ...
# Additionally, compare with math.pi to determine the error

import math

def main():
    print("Calculate an approximation for pi by summing a series")
    numTerms = int(input("Enter how many terms to use: "))
    
    total = 0
    for i in range(numTerms):
        total *= -1
        total += 4 / (2 * i + 1)
    
    total = abs(total)
    
    print("pi is approximately:", total)
    print("Error:", math.pi - total)

main()
