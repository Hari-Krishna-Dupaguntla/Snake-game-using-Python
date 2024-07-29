from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect the collision with the food
    if snake.head.distance(food)<15:
        snake.extedn()
        food.refresh()
        scoreboard.increase_score()
    #detect the collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset_score()
        snake.reset_snake()
        # game_is_on=False
        # scoreboard.game_is_over()
    #detect the collision with the tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset_score()
            snake.reset_snake()
            # game_is_on=False
            # scoreboard.game_is_over()

screen.exitonclick()
