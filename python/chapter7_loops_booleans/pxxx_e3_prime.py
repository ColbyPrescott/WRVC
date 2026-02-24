# Write a program that determines if a number is prime or not

import math

def is_prime(n):
    if n != 2 and n % 2 == 0:
        return False
    
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor += 2
    return True

def main():
    print("Prime number tester")
    n = int(input("Enter a value to test if it's prime: "))
    if is_prime(n):
        print(n, "is prime")
    else:
        print(n, "is not prime")

if __name__ == "__main__":
    main()