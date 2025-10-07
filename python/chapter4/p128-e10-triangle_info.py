# Let the user draw a triangle and print the perimeter and area

from graphics import *
import math

def main():
    win = GraphWin("Draw Triangle", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    p1 = win.getMouse()
    p1.draw(win)
    print("Point 1: (", p1.getX(), ", ", p1.getY(), ")", sep="")
    
    p2 = win.getMouse()
    p2.draw(win)
    print("Point 2: (", p2.getX(), ", ", p2.getY(), ")", sep="")
    
    p3 = win.getMouse()
    p3.draw(win)
    print("Point 3: (", p3.getX(), ", ", p3.getY(), ")", sep="")
    
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("darkslategray")
    triangle.draw(win)
    
    
    lengthA = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    lengthB = math.sqrt((p3.getX() - p2.getX()) ** 2 + (p3.getY() - p2.getY()) ** 2)
    lengthC = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    print("Side length A:", lengthA)
    print("Side length B:", lengthB)
    print("Side length C:", lengthC)
    
    s = (lengthA + lengthB + lengthC) / 2
    area = math.sqrt(s * (s - lengthA) * (s - lengthB) * (s - lengthC))
    print("Area:", area)
    
    win.getMouse()

main()