# The Sieve of Eratosthenes is an elegant algorithm for finding all of the prime numbers up to some limit n.
# The basic idea is to first create a list of numbers from 2 to n.
# The first number is removed from the list and announces as a prime number, and all multiple of this number up to n are removed from the list.
# This process continues until the list is empty.

def main():
    print("This program will find primes with the Sieve of Eratosthenes algorithm.")
    n = int(input("Enter a maximum number to search to: "))
    lst = list(range(2, n + 1))

    while len(lst) != 0:
        prime = lst[0]
        print(prime)
        lst = list(filter(lambda x: x % prime != 0, lst))
    
    print("Done")

if __name__ == "__main__":
    main()