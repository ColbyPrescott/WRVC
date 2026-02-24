# Upgrade triangle2.py to use a function to calculate the area of a triangle given length of three sides (from Chapter 3 Exercise 9)

import math
from graphics import *

def square(x):
    return x ** 2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def triangleArea(lengthA, lengthB, lengthC):
    s = (lengthA + lengthB + lengthC) / 2
    return math.sqrt(s * (s - lengthA) * (s - lengthB) * (s - lengthC))

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    
    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    
    lengthA = distance(p1, p2)
    lengthB = distance(p2, p3)
    lengthC = distance(p3, p1)
    area = triangleArea(lengthA, lengthB, lengthC)
    message.setText("Area: " + str(round(area, 2)))
    win.getMouse()
    
    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()

main()