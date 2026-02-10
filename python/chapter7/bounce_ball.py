from graphics import *
from random import randint

GRAVITY = 100
DELTA_TIME = 1 / 30
LEFT_EDGE = -200
RIGHT_EDGE = 200
TOP_EDGE = 200
BOTTOM_EDGE = -200

class Ball(Circle):
    def __init__(self, pos, radius, vel = Point(0, 0)):
        super().__init__(pos, radius)
        self.vel = vel
        self.friction = 0

    def translate(self):
        self.vel.y -= GRAVITY * DELTA_TIME / 2
        self.move(self.vel.x * DELTA_TIME, self.vel.y * DELTA_TIME)
        self.vel.y -= GRAVITY * DELTA_TIME / 2
    
    def bounce_x(self):
        self.vel.x *= -1
        self.vel.x *= 1 - self.friction
    
    def bounce_y(self):
        self.vel.y *= -1
        self.vel.y *= 1 - self.friction
    
    def collision(self):
        pos = self.getCenter()
        if pos.x - self.radius < LEFT_EDGE:
            pos.x = LEFT_EDGE + self.radius
            self.bounce_x()
        elif pos.x + self.radius > RIGHT_EDGE:
            pos.x = RIGHT_EDGE - self.radius
            self.bounce_x()
        if pos.y - self.radius < BOTTOM_EDGE:
            pos.y = BOTTOM_EDGE + self.radius
            self.bounce_y()
        elif pos.y + self.radius > TOP_EDGE:
            pos.y = TOP_EDGE - self.radius
            self.bounce_y()

    def update(self):
        self.translate()
        self.collision()


def main():
    win = GraphWin("Bouncing Ball", 500, 500)
    win.setCoords(LEFT_EDGE, BOTTOM_EDGE, RIGHT_EDGE, TOP_EDGE)

    balls = []

    vel_range = 100
    for i in range(10):
        ball = Ball(
            Point(0, 0), 
            20,
            Point(randint(-vel_range, vel_range), randint(-vel_range, vel_range))
        )
        ball.draw(win)
        balls.append(ball)

    while True:
        if win.checkMouse():
            break

        for ball in balls:
            ball.update()
        update(1 / DELTA_TIME)
    
    win.close()

if __name__ == "__main__":
    main()