import turtle
import math



area_input = int(input("Enter an integer between 2000 and 2500:  "))
area = area_input * 3
radius = math.sqrt(area/math.pi)

ryan = turtle.Turtle()
ryan.speed(0)
ryan.pencolor("red")
ryan.begin_fill()
ryan.circle(radius)
ryan.end_fill()
ryan.hideturtle()
