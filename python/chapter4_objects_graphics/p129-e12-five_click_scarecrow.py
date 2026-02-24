# Draw a scarecrow face with a circular head, triangle nose, circular eyes, and an oval for a mouth
# Click 1: Center of the head and top of the nose
# Click 2: Edge of the circular head
# Click 3: Lower left corner of the isosceles triangle nose
# Click 4: Center of the left eye (automatic 1/10 width of head, right eye is symmetric)
# Click 5: Lower left corner of mouth's oval (automatic horizontal centering and height of 1/10 head)

from graphics import *
import math

def distance(a, b):
    return math.sqrt((b.getX() - a.getX())**2 + (b.getY() - a.getY())**2)

def mirrorX(p, about):
    return Point(about.getX() + (about.getX() - p.getX()), p.getY())

def main():
    win = GraphWin("Scarecrow", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    message = Text(Point(0, -9), "")
    message.draw(win)
    
    message.setText("Click center of head")
    headCenter = win.getMouse()
    headCenter.draw(win)
    
    message.setText("Click edge of head")
    headEdge = win.getMouse()
    headRadius = distance(headCenter, headEdge)
    head = Circle(headCenter, headRadius)
    head.draw(win)
    
    message.setText("Click lower left corner of nose")
    noseBottomLeft = win.getMouse()
    noseBottomRight = mirrorX(noseBottomLeft, headCenter)
    nose = Polygon(noseBottomLeft, noseBottomRight, headCenter)
    nose.draw(win)
    
    message.setText("Click center of left eye")
    eyeRadius = headRadius / 10
    leftEyeCenter = win.getMouse()
    leftEye = Circle(leftEyeCenter, eyeRadius)
    leftEye.draw(win)
    rightEyeCenter = mirrorX(leftEyeCenter, headCenter)
    rightEye = Circle(rightEyeCenter, eyeRadius)
    rightEye.draw(win)
    
    message.setText("Click lower left corner of mouth")
    mouthHeight = headRadius / 5
    mouthBottomLeft = win.getMouse()
    mouthTopRight = Point(mirrorX(mouthBottomLeft, headCenter).getX(), mouthBottomLeft.getY() + mouthHeight)
    mouth = Oval(mouthBottomLeft, mouthTopRight)
    mouth.draw(win)
    
    message.setText("Click to colorize")
    win.getMouse()
    head.setFill("blue")
    nose.setFill("cornflowerblue")
    leftEye.setFill("green")
    rightEye.setFill("green")
    mouth.setFill("darkblue")
    
    message.setText("Beautiful. Click to exit")
    win.getMouse()

main()