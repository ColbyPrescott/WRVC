# The National Weather Service computed the windhcill index using the following formula:
# 35.74 + 0.6215T - 35.75(V^0.16)+0.4275T(V^0.16)
# Where T is the temperature in degrees Fahrenheit, and V is the wind speed in miles per hour
# Write a program that rpints a nicely formatted table of windchill values. 
# Rows should represent wind speed for 0 to 50 in 5-mph increments
# Columns represent temperatures from -20 to +60 in 10-degrees increments
# Note: THe formula only applies for wind speeds in excess of three miles per hour

def windchill_index(T, V):
    return 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)

def main():
    cell_width = 10
    spacer = "|"
    precision = 2

    wind_speeds = range(0, 55, 5)
    temperatures = range(-20, 70, 10)

    print(f"{spacer}{"Wind mph":^{cell_width}}{spacer}{"Temperature °F":^{(cell_width + len(spacer)) * len(temperatures) - len(spacer)}}{spacer}")
    temp_line = f"{spacer}{"":^{cell_width}}{spacer}"
    for T in temperatures:
        temp_line += f"{T:^{cell_width}.{precision}f}{spacer}"
    print(temp_line)
    print(f"{spacer}{"-" * cell_width}{spacer}{"-" * ((cell_width + len(spacer)) * len(temperatures) - len(spacer))}{spacer}")

    for V in wind_speeds:
        line = f"{spacer}{V:^{cell_width}}{spacer}"
        for T in temperatures:
            line += f"{windchill_index(T, V):^{cell_width}.{precision}f}{spacer}"
        print(line)

if __name__ == "__main__":
    main()