# Write a program to animate a circle bouncing around a window.
# The basic idea is to start the circle somewhere in the interior of the window.
# Use variables dx and dy (both initialized to 1) to control the movement of the circle.
# Bounce off edges

from graphics import *
import random

balls = []

class Ball:
    def __init__(self, win, pos=Point(0, 0)):
        self.win = win
        self.circle = Circle(pos, 1)
        self.dx = random.random() - 0.5
        self.dy = random.random() - 0.5

        self.circle.draw(self.win)
    
    def update(self):
        self.circle.move(self.dx, self.dy)

        if self.circle.getCenter().getX() < -10 + self.circle.getRadius():
            self.dx *= -1
            self.circle.move((-10 + self.circle.getRadius()) - self.circle.getCenter().getX(), 0)
        elif self.circle.getCenter().getX() > 10 - self.circle.getRadius():
            self.dx *= -1
            self.circle.move((10 - self.circle.getRadius()) - self.circle.getCenter().getX(), 0)
        
        if self.circle.getCenter().getY() < -10 + self.circle.getRadius():
            self.dy *= -1
            self.circle.move(0, (-10 + self.circle.getRadius()) - self.circle.getCenter().getY())
        elif self.circle.getCenter().getY() > 10 - self.circle.getRadius():
            self.dy *= -1
            self.circle.move(0, (10 - self.circle.getRadius()) - self.circle.getCenter().getY())

def main():
    win = GraphWin("Bouncing Ball", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    def onClick(point):
        balls.append(Ball(win, Point(
            point.getX() / 400 * 20 - 10,
            -(point.getY() / 400 * 20 - 10)
        ))) 

    win.setMouseHandler(onClick)

    for i in range(3):
        balls.append(Ball(win))

    while True:
        for ball in balls:
            ball.update()
        update(30)

if __name__ == "__main__":
    main()