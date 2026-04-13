from graphics import GraphWin, Point, Line

import os
print(os.getcwd())

def createWindow():
    win = GraphWin("Linear Regression", 500, 500)
    win.setCoords(0, 0, 10, 10)
    return win

def slope(xb, yb, xx, xy, n):
    # Returns the slope of the line of best fit, m
    return (xy - n * xb * yb) / (xx - n*xb*xb)

def predict(x, xb, yb, m):
    # Returns a predicated value for y
    return yb + m*(x-xb)

def processPoints(w, infile):
    # Points from infile and draw them into w
    # Returns: average of x values
    #          average of y values
    #          sum of the squares of the x values
    #          sum of the xy products
    #          the number of points clicked before Done
    sumX = 0.0
    sumY = 0.0
    sumXsq = 0.0
    sumXY = 0.0
    n = 0
    for line in infile:
        x, y = [float(num) for num in line.split()]
        Point(x, y).draw(w)
        sumX = sumX + x
        sumY = sumY + y
        sumXY = sumXY + x * y
        sumXsq = sumXsq + x * x
        n = n + 1
    return sumX/n, sumY/n, sumXsq, sumXY, n

def main():
    win = createWindow()
    fname = input("Enter name of file containing point data: ")
    with open(fname, "r") as infile:
        xbar, ybar, sumXsq, sumXY, n = processPoints(win, infile)
    m = slope(xbar, ybar, sumXsq, sumXY, n)
    y1 = predict(0, xbar, ybar, m)
    y2 = predict(10, xbar, ybar, m)
    regLine = Line(Point(0, y1), Point(10, y2))
    regLine.setWidth(2)
    regLine.draw(win)
    input("Press <Enter> to quit")
    win.close()

if __name__ == "__main__":
    main()