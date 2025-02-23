import random
from turtle import Turtle
from snake import Snake
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.setposition(random.randint(-230, 230), random.randint(-230, 230))


