from graphics import *

def main():
    win = GraphWin()
    
    radius = 20
    colors = ["white", "black", "blue", "red", "yellow"]
    
    for i in range(len(colors)):
        circle = Circle(Point(100, 100), radius * (len(colors) - i))
        circle.setFill(colors[i])
        circle.setOutline(colors[i])
        circle.draw(win)
    
    win.getMouse()

main()