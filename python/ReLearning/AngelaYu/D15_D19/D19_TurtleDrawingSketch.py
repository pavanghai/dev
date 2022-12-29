from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward(): tim.forward(10)


def move_backward(): tim.backward(10)


def turn_left(): tim.left(10)


def turn_right(): tim.right(10)


def clear(): tim.reset()


screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=turn_left)
screen.onkey(turn_right, "D")
screen.onkey(key="C", fun=clear)
screen.exitonclick()
