# Compute nth number in Fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13, 21, etc...

def main():
    print("Compute the Nth number in the Fibonacci sequence")
    
    n = int(input("Enter the number to find: "))
    
    a = 0 # Starts at 0 so Fibonacci programming index 0 can return 0 and natural index 1 can return the given definition of the sequence. Seems like a fitting match to me
    b = 1
    for i in range(n):
        sum = a + b
        a = b
        b = sum
    
    print("Fibonacci number #", n, " is: ", a, sep="")

main()
