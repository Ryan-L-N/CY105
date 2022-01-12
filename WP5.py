import math

angle = float(input("Enter an angle:  "))
deg_or_rad = input("Did you enter 'degrees' or 'radians'?  ")
size = input("What size pizza did you order?  ")

if size == "small":
    radius = 10
elif size == "medium":
    radius = 12
elif size == "large":
    radius = 14
else:  
    radius = 16

if deg_or_rad == "radians":
    angle = math.degrees(angle)

arc_length = 2 * math.pi * radius * angle/360

print("The arc length is: ", arc_length)
