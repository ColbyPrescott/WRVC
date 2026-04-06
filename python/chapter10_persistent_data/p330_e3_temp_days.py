# Rewrite Exercise 8 from Chapter 7 to get its data from a file

from tkinter.filedialog import askopenfilename

def main():
    print("This program estimates the amount of energy used in heating and cooling.")
    print("Select the file with the average temperature in degrees Fahrenheit for each day.")
    print()

    day = 1
    heating = 0
    cooling = 0
    filename = askopenfilename()
    if filename == "":
        print("Goodbye!")
        return
    with open(filename, "r") as infile:
        for line in infile:
            temp = float(line)
            if temp < 60:
                heating += 60 - temp
            elif temp > 80:
                cooling += temp - 80
            
            day += 1
    
    print("Total degrees warmed:", heating)
    print("Total degrees cooled:", cooling)

if __name__ == "__main__":
    main()