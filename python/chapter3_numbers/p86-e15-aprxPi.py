# Calculate an approximation for pi by summing a certain series, with the user inputting the number of terms
# Series: (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) ...
# Additionally, compare with math.pi to determine the error

import math

def main():
    print("Calculate an approximation for pi by summing a series")
    numTerms = int(input("Enter how many terms to use: "))
    
    total = 0
    for i in range(numTerms):
        if i % 2 == 0:
            total += 4 / (2 * i + 1)
        else:
            total -= 4 / (2 * i + 1)
    
    print("pi is approximately:", total)
    print("Error:", math.pi - total)

main()
