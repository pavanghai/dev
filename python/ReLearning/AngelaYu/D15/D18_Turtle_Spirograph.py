from random import choice, randint
import turtle as t

c_draw = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    r_color = (r, g, b)
    return r_color


c_draw.speed('fastest')
c_draw.pensize(3)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        c_draw.color(random_color())
        c_draw.circle(50)
        c_draw.setheading(c_draw.heading() + size_of_gap)


draw_spirograph(25)

screen = t.Screen()
screen.exitonclick()
