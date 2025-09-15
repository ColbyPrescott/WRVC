# p30-e8-chaos.py by Colby Prescott 9/8/25
# Two input values

def main():
    print("This program illustrates a chaotic function in two columns")
    x = float(input("Enter seed X between 0 and 1: "))
    y = float(input("Enter seed Y between 0 and 1: "))
    print("Iteration         X                        Y")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(i + 1, "        ", x, "   ", y)

main()