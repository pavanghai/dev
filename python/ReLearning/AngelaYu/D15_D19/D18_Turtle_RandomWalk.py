from random import choice, randint
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    r_color = (r, g, b)
    return r_color


distance = 25
angle = (0, 90, 180, 270)
tim.pensize(5)
tim.speed('fastest')

for _ in range(1000):
    tim.forward(distance)
    tim.setheading(choice(angle))
    tim.color(random_color())