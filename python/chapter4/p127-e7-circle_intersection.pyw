# Compute and display the intersection between a circle of suer input and a horizontal line at a specific y-intercept

from graphics import *
import math

def main():
    radius = float(input("Enter the circle radius: "))
    intercept = float(input("Enter the horizontal line y-intercept: "))
    
    if abs(intercept) > radius:
        print("No intersection :(")
        return
    
    intersection = math.sqrt(radius**2 - intercept**2)
    print("Intersection 1: (", -intersection, ", 10)", sep="")
    print("Intersection 2: (", intersection, ", 10)", sep="")
    
    win = GraphWin("Circle Intersection")
    win.setCoords(-10, -10, 10, 10)
    
    circle = Circle(Point(0, 0), radius)
    circle.setFill("darkslategray")
    circle.draw(win)
    
    Line(Point(-10, intercept), Point(10, intercept)).draw(win)
    
    point1 = Point(-intersection, intercept)
    point1.setFill("red")
    point1.draw(win)
    
    point2 = Point(intersection, intercept)
    point2.setFill("red")
    point2.draw(win)
    
    win.getMouse()

main()