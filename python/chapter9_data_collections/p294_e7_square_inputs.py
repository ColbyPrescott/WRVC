# Use the functions from the previous two exercises to program a program that computes the sum of the squares of numbers that the user enters on a single line of input

from p294_e6_num_each import toNumbers
from p294_e5_square_each import squareEach

def main():
    lst = []
    while True:
        inp = input("Enter a number (<Enter> to end): ")
        if inp != "":
            lst.append(inp)
        else:
            break
    
    toNumbers(lst)
    squareEach(lst)

    print("Squares:", lst)

if __name__ == "__main__":
    main()