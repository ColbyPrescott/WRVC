# Write an improved version of futval.py from Chapter 2.
# The new version will prompt th euser for the amount of the investment, the annualized interest rate, and the number of years of the investment.
# The program will then output a niceley formatted table that tracks the value of the investment year by year

def main():
    print("This program will calculate the future value of an investment after some number of years.")
    
    value = float(input("Enter the starting investment ($): "))
    rate = float(input("Enter the annualized interest rate (%): "))
    years = int(input("Enter the number of years to calcualte (#): "))

    year_width = 6
    value_width = 10
    spacer = " | "

    print(f"{"Year":^{year_width}}{spacer}{"Value":^{value_width}}")
    print("-" * (year_width + len(spacer) + value_width))

    for i in range(years + 1):
        print(f"{i:^{year_width}}{spacer}{("$" + f"{value:.2f}"):^{value_width}}")
        value *= 1 + rate / 100
    
if __name__ == "__main__":
    main()