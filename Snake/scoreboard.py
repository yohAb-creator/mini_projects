from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(150, 300)
        self.score = 0
        self.setposition(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_score()


    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.color("red")
        self.setposition(0, 0)
        self.write(f"Game over! \n Score: {self.score}", align="center", font=("Arial", 30, "normal"))


