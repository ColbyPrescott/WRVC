# Redo Chapter 7 Exercise 7 so that it gets its input from a file

# Program to figure out gas milage over a multiple-leg journey

from tkinter.filedialog import askopenfilename

def main():
    print("This program calculates fuel efficiency over a multi-leg journey.")
    print("Start with your initial odometer reading with a full tank of gas.")
    print("For each leg, enter the number gallons needed to fill the tank and")
    print("the odometer reading at the time of fill.")
    print()

    distance = 0.0
    total_fuel = 0.0
    prev_odometer = float(input("Enter odometer reading at trip start: "))
    print()
    print("Choose the file with the trip information.")
    print("Each line should be formatted as \"<new odometer reading>, <gallons used since last odometer reading>\"")
    filename = askopenfilename()
    if filename == "":
        print("Goodbye!")
        return
    with open(filename, "r") as infile:
        i = 0
        for line in infile:
            i += 1
            odometer, gallons = map(lambda x: float(x), line.split(", "))
            miles = odometer - prev_odometer
            prev_odometer = odometer
            print(f"MPG for leg #{i}:", round(miles / gallons, 1))
            distance += miles
            total_fuel += gallons
    
    print()
    print("You traveled a total of", round(distance, 1),
          "miles on", total_fuel, "gallons.")
    print("You got an average of", round(distance/total_fuel, 1), "miles per gallon")

if __name__ == "__main__":
    main()