

from snake import Snake, Screen
from food import Food
from scoreboard import Scoreboard
import random
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorer = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()



    time.sleep(0.0)

    snake.move()
    # Snake consumes food
    if snake.segments[0].distance(food) < 15:
        food.setposition(random.randint(-230, 230), random.randint(-230, 230))
        snake.add_segment()
        scorer.increase_score()
    # Wall collision
    if not (-300 < snake.segments[0].xcor() < 300 and -300 < snake.segments[0].ycor() <= 300):
        print("Collided with wall. Game over!")
        print(f"Score: {scorer.score}")
        scorer.game_over()
        game_is_on = False
    # Snake bites own tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment.position()) < 0.1:
            print(f"Game over! Score: {scorer.score}")
            scorer.game_over()
            game_is_on = False




screen.exitonclick()