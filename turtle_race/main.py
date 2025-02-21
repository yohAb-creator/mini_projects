import random
from turtle import Turtle, Screen

colors = ["red", "green", "blue", "pink", "black"]

turtles = []
screen = Screen()
screen.setup(width=500, height=400)
y_in = -100
for color in colors:
    tim = Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(color)
    tim.setposition(-230, y_in)
    y_in += 30
    turtles.append(tim)






destination = 0
guess = screen.textinput("Good luck!", "Choose which turtle to bet on.")
winner = []
while destination < 230:
    for tim in turtles:
        if tim.xcor() > destination:
            destination = tim.xcor()
            winner = tim.color()
    for tim in turtles:
        tim.forward(random.randint(1, 10))
if guess == winner[0]:
    print(f"You win!")
else:
    print(f"You lose! {winner[0]} wins")




screen.exitonclick()