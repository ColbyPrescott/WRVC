def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = float(input("Enter the initial principal: "))
    rate = float(input("Enter the nominal rate as decimal: "))
    periods = int(input("Enter the number of compounds per year: "))
    
    total = principal
    for i in range(10 * periods):
        total = total * (rate / periods + 1)
    
    print("The value in 10 years is:", total)

main()