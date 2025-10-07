# Click 1: Bottom left of house
# Click 2: Top right of house
# Click 3: Center of top edge of door
# Click 4: Center of window
# Click 5: Top of the roof

from graphics import *

def main():
    win = GraphWin("Draw a house!", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    message = Text(Point(0, 9), "")
    message.draw(win)
    
    message.setText("Click the bottom left corner of the house")
    houseBottomLeft = win.getMouse()
    houseBottomLeft.draw(win)
    
    message.setText("Click the top right corner of the house")
    houseTopRight = win.getMouse()
    
    house = Rectangle(houseBottomLeft, houseTopRight)
    house.draw(win)
    
    
    message.setText("Click the top center of the door")
    doorTopCenter = win.getMouse()
    
    doorWidth = 2
    doorBottomLeft = Point(doorTopCenter.getX() - doorWidth / 2, houseBottomLeft.getY())
    doorTopRight = Point(doorTopCenter.getX() + doorWidth / 2, doorTopCenter.getY())
    door = Rectangle(doorBottomLeft, doorTopRight)
    door.draw(win)
    
    
    message.setText("Click the center of the window")
    windowCenter = win.getMouse()
    
    windowSize = 2
    windowBottomLeft = Point(windowCenter.getX() - windowSize / 2, windowCenter.getY() - windowSize / 2)
    windowTopRight = Point(windowCenter.getX() + windowSize / 2, windowCenter.getY() + windowSize / 2)
    window = Rectangle(windowBottomLeft, windowTopRight)
    window.draw(win)
    
    message.setText("Click the top of the roof")
    roofTop = win.getMouse()
    Line(roofTop, Point(houseBottomLeft.getX(), houseTopRight.getY())).draw(win)
    Line(roofTop, Point(houseTopRight.getX(), houseTopRight.getY())).draw(win)
    
    message.setText("You did it wrong :(\nClick to exit") # Encouragement    win.getMouse()

main()