# Let user draw a rectangle and report the area and perimeter

from graphics import *

def main():
    win = GraphWin("Draw Rectangle", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    p1 = win.getMouse()
    p1.draw(win)
    print("Point 1: (", p1.getX(), ", ", p1.getY(), ")", sep="")
    
    p2 = win.getMouse()
    p2.draw(win)
    print("Point 2: (", p2.getX(), ", ", p2.getY(), ")", sep="")
    
    rect = Rectangle(p1, p2)
    rect.setFill("darkslategray")
    rect.draw(win)
    
    width = abs(p2.getX() - p1.getX())
    height = abs(p2.getY() - p1.getY())
    area = width * height
    perimeter = 2 * (width + height)
    
    print("Width:", width)
    print("Height:", height)
    print("Area:", area)
    print("Perimeter:", perimeter)
    
    win.getMouse()

main()