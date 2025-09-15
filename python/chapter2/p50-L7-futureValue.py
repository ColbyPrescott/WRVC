def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual percentage rate as decimal: "))
    
    for i in range(10):
        principal = principal * (1 + apr)
    
    print("The value in 10 years is:", principal)

main()