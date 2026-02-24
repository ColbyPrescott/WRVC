# Calculate the shipping price for coffee that sells at $15.50 a pound, plus shipping of$4.50 plus $0.99 per pound

def main():
    print("Flavor 'Coffee': $15.50 per pound")
    print("Shipping is $4.50 plus $0.99 a pound")
    
    weight = float(input("How many POUNDS of coffee you want to order? "))
    
    total = 15.50 * weight
    total += 4.50
    total += 0.99 * weight
    
    print("Final order total: $", total, sep="")

main()