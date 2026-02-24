# Determine distance to lightning strike based on time elapsed between flash and sound of thunder.
# Speed of sound is about 1100 ft/sec
# 1 mile is 5280 ft

def main():
    seconds = float(input("Enter number of seconds between flash and sound: "))
    
    distFt = 1100 * seconds
    distMi = distFt / 5280
    
    print("The lightning is", distMi, "miles away")

main()