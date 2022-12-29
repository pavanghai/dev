from turtle import Turtle, Screen


def draw_dash_line(n, obj):
    dash = 10
    for _ in range(n):
        obj.forward(dash)
        obj.penup()
        obj.forward(dash)
        obj.pendown()


t = Turtle()
t.shape("arrow")
t.color("black")
draw_dash_line(15, t)

screen = Screen()
screen.exitonclick()
