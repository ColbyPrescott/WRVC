# Write a `moveTo(shape, newCenter)` function where `shape` is a graphics object with a `getCenter` function
# Use this function to write a program that draws a circle and then allows the user to click the window 10 times. Each time the suer clicks, the circle is moved where the user clicked.

from graphics import *

def moveTo(shape, newCenter):
    dx = newCenter.getX() - shape.getCenter().getX()
    dy = newCenter.getY() - shape.getCenter().getY()
    shape.move(dx, dy)

def main():
    win = GraphWin("Move Circle", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    circle = Circle(win.getMouse(), 3)
    circle.draw(win)
    
    for i in range(10):
        moveTo(circle, win.getMouse())
    
    win.getMouse()

main()