def main():
    print("This program calculates the future value")
    print("of an investment after some number of years.")
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual percentage rate as decimal: "))
    years = int(input("Enter how many years have passed: "))
    
    for i in range(years):
        principal = principal * (1 + apr)
    
    print("The value in", years, "year" if years == 1 else "years", "is:", principal)

main()