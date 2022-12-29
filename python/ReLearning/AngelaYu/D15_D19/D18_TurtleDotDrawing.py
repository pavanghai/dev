from random import choice
import turtle as t

import colorgram

# Read colors from existing picture
def color_list(file, no_of_colors):
    """returns the list of rbg colors from an image, ignoring the major color"""
    colors = colorgram.extract(file,no_of_colors)[2:]
    return [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]


# create 10 x 10 painting from the color list
colors = color_list('D18_HirstPainting.jpg',30)
t.colormode(255)
screen = t.Screen()
screen.setworldcoordinates(-400,-300, screen.window_width(), screen.window_height())
dot = t.Turtle()
dot.speed('fastest')
dot.hideturtle()
dot.penup()

for _ in range(10):
    dot.setpos(0.00, _ * 50.00)
    for _ in range(10):
        dot.dot(20, choice(colors))
        dot.fd(50)

screen.exitonclick()
