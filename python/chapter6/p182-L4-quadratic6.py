import math

def main():
    print("This program finds the real solutions to a quatratic\n")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        discRoot = math.sqrt(b * b - 4 * a *c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        print("\nThe solutions are:", root1, root2) 
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nNo real roots")
        else:
            print("\nInvalid coefficient given")
    except:
        print("\nTeehee something went very wrong, oopsies! Not gonna tell you what it was X3")

if __name__ == "__main__":
    main()