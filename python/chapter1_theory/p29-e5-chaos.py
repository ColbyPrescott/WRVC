def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    numLoops = int(input("Enter a number of times to iterate the loop: "))
    for i in range(numLoops):
        x = 3.9 * x * (1 - x)
        print(x)

main()