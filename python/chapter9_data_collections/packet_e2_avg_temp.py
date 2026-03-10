# Collect 7 daily temperatures. Calculate the average temperature, and count how many days were above the average

def main():
    print("Enter 7 daily temperatures")
    temps = []
    for i in range(7):
        temp = float(input(f"Enter temperature {i + 1}/7: "))
        temps.append(temp)
    
    avg = sum(temps) / len(temps)
    print("Average temeprature:", avg)

    high_temps = 0
    for temp in temps:
        if temp > avg:
            high_temps += 1
    print(f"{high_temps} {"day was" if high_temps == 1 else "days were"} above the average")


if __name__ == "__main__":
    main()