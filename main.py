from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
score = Scoreboard()
snake_x = snake.head.xcor()
snake_y = snake.head.ycor()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(snake.down, 'Down')
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_point()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        food.reset()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
