def main():
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    x3 = float(input("x3: "))

    maxval = x1

    if x2 > maxval:
        maxval = x2
    if x3 > maxval:
        maxval = x3
    
    print("Max value:", maxval)

if __name__ == "__main__":
    main()