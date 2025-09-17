# Calculate an approximation of the square root of a number using Newton's method
# Newton's method:
#   Let "x" be the target number to square root
#   Let "guess" be the current approximation of the square root
#   "guess" should start as x / 2
#   The guess can be improved by iterating:
#       guess = (guess + (x / guess)) / 2

# I assumed I would have to research Newton's method after how much it was hyped up, but turns out the book provides enough context itself
# Granted, I think I have also seen this method demonstrated in a Vsauce video before

def main():
    print("Calculate an approximation of the square root of a number using Newton's method.")
    print()
    
    x = float(input("Enter a number to take the square root of: "))
    iterations = int(input("Enter a number of iterations to perform: "))
    
    guess = x / 2
    for i in range(iterations):
        guess = (guess + (x / guess)) / 2
    
    print("Final approximation:", guess)

main()
