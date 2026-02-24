def main():
    print("This program estimates the amount of energy used in heating and cooling.")
    print("Enter the average temperature in degrees Fahrenheit for each day. Hit <Enter> to stop.")
    print()

    day = 1
    heating = 0
    cooling = 0
    inp = input("Avg °F on day " + str(day) + ": ")
    while inp != "":
        temp = float(inp)
        if temp < 60:
            heating += 60 - temp
        elif temp > 80:
            cooling += temp - 80
        
        day += 1
        inp = input("Avg °F on day " + str(day) + ": ")
    
    print()
    print("Total degrees warmed:", heating)
    print("Total degrees cooled:", cooling)

if __name__ == "__main__":
    main()