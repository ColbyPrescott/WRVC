# Modify p126-d3-circle.pyw to
# a) Make it draw squares instead of circles
# b) Draw new squares instead of moving the existing one
# c) Print "Click again to quit" after the loop ends

from graphics import *

def main():
    win = GraphWin()
    
    for i in range(10):
        p = win.getMouse()
        size = 20
        shape = Rectangle(Point(p.getX() - size, p.getY() - size), Point(p.getX() + size, p.getY() + size))
        # Could also use clone
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    
    Text(Point(100, 100), "Click again to quit :3").draw(win)
    win.getMouse()
    
    win.close()

main()