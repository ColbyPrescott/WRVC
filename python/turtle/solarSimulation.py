import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System")
screen.setup(600, 600)
screen.tracer(0)

class Sun:
    def __init__(self, radius):
        self.radius = radius
        self.x = 0
        self.y = 0
        self.turtle = turtle.Turtle()

        self.turtle.color("yellow")
        self.turtle.penup()
        self.turtle.goto(self.x, self.y - self.radius)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()
        self.turtle.penup()

        self.turtle.hideturtle()

class Planet:
    def __init__(self, name, radius, orbit_radius, speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.color = color
        self.angle = 0
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(self.color)

        # TODO #1

        self.turtle.penup()
        self.turtle.goto(self.orbit_radius, 0)

        # CHALLENGE

    def move(self):
        # All the TODOs
        pass

sun = Sun(50)
planet = Planet("Wowie", 30, 100, 5, "blue")
screen.update()

input()