# The values now tend toward 0.5 whenever the program is run, unless 0 or 1 is input

def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()