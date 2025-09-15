def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickles * 0.05 + pennies * 0.01
    print()
    print("The total of your change is", total)

main()