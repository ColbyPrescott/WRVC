# Program to figure out gas milage over a multiple-leg journey

def main():
    print("This program calculates fuel efficiency over a multi-leg journey.")
    print("Start with your initial odometer reading with a full tank of gas.")
    print("For each leg, enter th enumber gallongs needed to fill the tank and")
    print("the odometer reading at the time of fill.")
    print()

    distance = 0.0
    total_fuel = 0.0
    odometer = float(input("Enter odometer reading at trip start: "))
    print()
    str_in = input("Enter gallons used for current leg (<Enter> to quit): ")
    while str_in != "":
        gallons = float(str_in)
        odometer1 = float(input("Enter odometer reading: "))
        miles = odometer1 - odometer
        odometer = odometer1
        print("MPG for this leg:", round(miles / gallons, 1))
        distance += miles
        total_fuel += gallons
        print()
        str_in = input("Enter gallons used for current leg (<Enter> to quit): ")
    
    print()
    print("You traveled a total of", round(distance, 1),
          "miles on", total_fuel, "gallons.")
    print("You got an average of", round(distance/total_fuel, 1), "miles per gallon")

if __name__ == "__main__":
    main()