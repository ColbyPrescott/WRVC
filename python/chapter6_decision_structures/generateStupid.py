def main():
    numVals = 10

    for i in range(numVals):
        print("x", i, " = int(input(\"x", i, ": \"))", sep="")
    
    print()
    print("maxval = x0")
    print()

    for i in range(1, numVals):
        print("if x", i, " > maxval:", sep="")
        print("    maxval = x", i, sep="")

main()