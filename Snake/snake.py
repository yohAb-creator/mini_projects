from turtle import Turtle, Screen
import time


INIT = [0, -20, -40]
MOVE_DISTANCE = 20
screen = Screen()
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            self.segments.append(t)

        for i in range(len(self.segments)):
            self.segments[i].goto(INIT[i], 0)
    game_is_on = True
    def move(self):
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.controls()
    def moveup(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)

    def movedown(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(270)

    def moveleft(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180)
    def moveright(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0)
    def controls(self):
        screen.listen()
        screen.onkey(key="Up", fun=self.moveup)
        screen.onkey(key="Down", fun=self.movedown)
        screen.onkey(key="Left", fun=self.moveleft)
        screen.onkey(key="Right", fun=self.moveright)

    def add_segment(self):
        t = Turtle(shape="square")
        t.setposition(self.segments[-1].position())
        t.color("white")
        t.penup()
        self.segments.append(t)



