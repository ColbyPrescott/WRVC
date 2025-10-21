# Upgrade Chapter 3 Exercise 16 Fibonacci to use a function that computes the nth digit

def fibonacci(n):
    a = 0 # Starts at 0 so Fibonacci programming index 0 can return 0 and natural index 1 can return the given definition of the sequence. Seems like a fitting match to me
    b = 1
    for i in range(n):
        sum = a + b
        a = b
        b = sum
    
    return a

def main():
    n = int(input("Enter the nth number to find: "))
    
    print("Fibonacci number #", n, " is: ", fibonacci(n), sep="")

main()