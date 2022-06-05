from re import S
import turtle as tur
from snake import Snake
import time

screen = tur.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

game_is_on = True


#create snake body
game_snake = Snake()
screen.listen()
screen.onkey(game_snake.up,"Up")
screen.onkey(game_snake.down,"Down")
screen.onkey(game_snake.left,"Left")
screen.onkey(game_snake.right,"Right")


while game_is_on:
    screen.update()
    time.sleep(.1)
    game_snake.move()
    


#move the snake

#create snake food

#detect collision with food

#create scoreboard

#detect collision with wall

#detect collision with tail

screen.exitonclick()