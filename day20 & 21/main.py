from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor('black')
screen.title('Snake game')  
screen.tracer(0)
score = Scoreboard()
snake = Snake()
fods = Food()
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
    
    #Detect collision with food class
    if snake.segments[0].distance(fods) < 15:
        fods.refresh()
        score.update()
        snake.increase_size()
        
    
    #detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        score.gameover()
        screen.update()
        game_is_on = False
    
    #detect collision with tail
    leng = len(snake.segments)
    for snaked in snake.segments[1:leng]:
        if snake.segments[0].distance(snaked) <10:
            score.gameover() 
            screen.update()
            game_is_on = False

screen.exitonclick()
