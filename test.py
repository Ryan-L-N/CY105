import turtle
import math

ryan = turtle.Turtle()
world = turtle.Screen()
ryan.speed(0)
ryan.shape("turtle")
ryan.goto(-180,0)
ryan.pensize(5)
world.bgcolor("black")

for x in range(-180, 180):
    x_rad = math.rad(x)
    y = math.sin(x_rad)
    ryan.goto(x,y)
    if x < -60:
        ryan.pencolor("red")
    elif x < 60:
        ryan.pencolor("white")
    else:
        ryan.pencolor("blue")

    