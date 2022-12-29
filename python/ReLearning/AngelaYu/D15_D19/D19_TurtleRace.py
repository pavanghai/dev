from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ("red", "orange", "yellow", "green", "blue", "purple")
# turtle_names = ["tim"+str(x) for x in range(1,len(colors)+1)]
all_turtle = []
# for i, tim in enumerate(turtle_names):
for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=(-100+(i*40)))
    all_turtle.append(tim)

is_race_on = False
if user_bet: is_race_on = True
while is_race_on:
    for tim in all_turtle:
        if tim.xcor()>230:
            is_race_on = False
            winning_color = tim.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner! ")
        rand_distance = randint(0,10)
        tim.forward(rand_distance)

screen.exitonclick()