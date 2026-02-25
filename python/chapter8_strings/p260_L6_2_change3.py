# Aprogram to calculate the value of some change in dollars

def main():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
    dollars, cents = divmod(total, 100)

    print(f"The total of your change is ${dollars}.{cents:0>2}.")

if __name__ == "__main__":
    main()