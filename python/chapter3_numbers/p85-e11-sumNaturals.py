# Calcualte the sum of the first n natural numbers

def main():
    print("Calculate the sum of the first n natural numbers")
    n = int(input("Enter number of natural numbers: "))
    
    total = 0
    # Zero is not a natural number but it is still fine to loop through because adding zero does nothing
    for i in range(n + 1):
        total += i
    
    print("Sum:", total)

main()
