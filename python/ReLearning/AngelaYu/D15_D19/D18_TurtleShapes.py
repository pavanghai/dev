from random import choice
from turtle import Turtle, Screen


def draw_shapes(sides, size, obj):
    angle = 360/sides
    for _ in range(sides):
        obj.right(angle)
        obj.forward(size)


clr = ('red', 'green', 'orange', 'blue', 'dark green')
s = Turtle()
s.shape("arrow")
s.color("black")

for side in range(3, 11):
    s.pencolor(choice(clr))
    draw_shapes(side, 100, s)

screen = Screen()
screen.exitonclick()
