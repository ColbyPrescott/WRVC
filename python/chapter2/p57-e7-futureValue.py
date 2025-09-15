def main():
    print("This program calculates the future value")
    print("of a compound investment after some number of years.")
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual percentage rate as decimal: "))
    years = int(input("Enter how many years have passed: "))
    
    total = 0
    for i in range(years):
        total += principal
        total = total * (1 + apr)
        print("The value in", i+1, "year" if i+1 == 1 else "years", "is:", total)

main()