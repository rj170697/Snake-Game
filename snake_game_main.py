from turtle import Turtle,Screen
import time
from snake import Snake
from food_snake import Food
from score_board import Score_board

screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor('black')
screen.title('My Snake Game')
player_1=screen.textinput(title='snake game',prompt='name?')
player=Score_board(player_1)
snake=Snake('timmy')
screen.tracer(0)
food=Food()

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    snake.signal()
    snake.move()
    if snake.snake_body[0].xcor()<-400 or snake.snake_body[0].xcor()>400 or snake.snake_body[0].ycor()<-400 or snake.snake_body[0].ycor()>400:
        game_on=False
        print(player.score)
    for i in snake.snake_body[1:]:
        if snake.snake_body[0].distance(i)<10:
            game_on=False
            print(player.score)



    if snake.snake_body[0].distance(food)<15:
        print('nom nom')
        snake.add_sgmnts()
        food.move()
        player.up_score()
        player.score_update()



























screen.exitonclick()

