# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when the paddle misses
# Keep score

from turtle import Screen
from paddle import Paddle
import time
from ball import PingPong

#Screen setup
screen = Screen()
screen.setup(700,600)
screen.title('Ping pong game')
screen.bgcolor('black')
screen.tracer(0)

player1_paddle = Paddle()
player1_paddle.goto(-335,0)
player2_paddle = Paddle()
player2_paddle.goto(330,0)
pingpong = PingPong() 

game_is_on = True
screen.listen()
screen.onkeypress(player1_paddle.south,'s')
screen.onkeypress(player1_paddle.north,'w') 
screen.onkeypress(player2_paddle.south,'Down')
screen.onkeypress(player2_paddle.north,'Up')

while game_is_on:

    screen.update()
    pingpong.move()
    #collision with wall with player paddle
    player1_paddle.check_wall_collision()
    player2_paddle.check_wall_collision()
    time.sleep(0.1)

    
    

screen.exitonclick()
