def main():
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    x3 = float(input("x3: "))

    if x1 >= x2 and x1 >= x3:
        print("Max is x1:", x1)
    elif x2 >= x3:
        print("Max is x2:", x2)
    else:
        print("Max is x3:", x3)

if __name__ == "__main__":
    main()