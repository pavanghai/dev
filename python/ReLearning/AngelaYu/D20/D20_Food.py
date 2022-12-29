from random import randint, randrange
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.setheading(randrange(0, 361, 20))
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)
