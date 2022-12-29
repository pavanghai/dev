from turtle import Turtle, Screen


def draw_square(size, obj):
    """
    Draw square with turtle object
    Args:
        size(int): size of square to draw
        obj(turtle object): pass object name
    returns:
        None
    """
    for _ in range(4):
        # obj.forward(size)
        obj.right(90)
        obj.forward(size)


sq = Turtle()
sq.shape("arrow")
sq.color("black")
draw_square(100, sq)

screen = Screen()
screen.exitonclick()
