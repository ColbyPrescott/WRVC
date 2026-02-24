# Calculate slope for line (x1, y1), (x2, y2)

def main():
    print("Calculate slope of line with points (x1, y1) and (x2, y2)")
    
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    slope = (y2 - y1) / (x2 - x1)
    
    print("Slope of the line:", slope)

main()