from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')  
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkeypress(snake.north,'Up')
screen.onkeypress(snake.west, 'Left')
screen.onkeypress(snake.south, 'Down')
screen.onkeypress(snake.east, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
  
    snake.move()

screen.exitonclick()