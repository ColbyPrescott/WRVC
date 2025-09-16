# Calculate the sum of a series of numbers entered by the user

def main():
    print("Calculate the sum of some numbers")
    numInputs = int(input("Enter how many numbers to input: "))
    
    total = 0
    for i in range(numInputs):
        num = float(input(str(i + 1) + ". Enter a number: "))
        total += num
    
    print("Sum:", total)

main()
