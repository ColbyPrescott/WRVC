# Solve Chapter 3 Exercise 17 with a `nextGuess(guess, x)` function

# Calculate an approximation of the square root of a number using Newton's method
# Newton's method:
#   Let "x" be the target number to square root
#   Let "guess" be the current approximation of the square root
#   "guess" should start as x / 2
#   The guess can be improved by iterating:
#       guess = (guess + (x / guess)) / 2

def nextGuess(guess, x):
    return (guess + (x / guess)) / 2

def main():
    print("Calculate an approximation of the square root of a number using Newton's method.")
    print()
    
    x = float(input("Enter a number to take the square root of: "))
    iterations = int(input("Enter a number of iterations to perform: "))
    
    guess = x / 2
    for i in range(iterations):
        guess = nextGuess(guess, x)
    
    print("Final approximation:", guess)

main()
