# Compute the molecular weight of a carbohydrate given the number of hydrogen, carbon, and oxygen atoms

def main():
    numHydrogen = int(input("Enter # hydrogen atoms: "))
    numCarbon = int(input("Enter # carbon atoms: "))
    numOxygen = int(input("Enter # oxygen atoms: "))
    
    # Grams per mole pulled from page 84
    hydrogenWeight = 1.00794
    carbonWeight = 12.0107
    oxygenWeight = 15.9994
    
    weight = numHydrogen * hydrogenWeight + numCarbon * carbonWeight + numOxygen * oxygenWeight
    print("Molecular weight of the carbohydrate:", weight)

main()