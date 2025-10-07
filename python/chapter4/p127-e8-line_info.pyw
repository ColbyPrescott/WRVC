# Let the user click two points to draw a line, then print out the length and slope

from graphics import *
import math

def main():
    win = GraphWin("Line Info", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    p1 = win.getMouse()
    p1.draw(win)
    print("Point 1: (", p1.getX(), ", ", p1.getY(), ")", sep="")
    
    p2 = win.getMouse()
    p2.draw(win)
    print("Point 2: (", p2.getX(), ", ", p2.getY(), ")", sep="")
    
    Line(p1, p2).draw(win)
    
    length = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    print("Length:", length)
    
    if p1.getX() != p2.getX():
        slope = (p2.getY() - p1.getY()) / (p2.getX() - p1.getX())
        print("Slope:", slope)
    else:
        print("Slope: undefined (vertical line)")
    
    win.getMouse()

main()