# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when the paddle misses
# Keep score

from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import PingPong
from scoreboard import Scoreboard

def refresh(flag):
    global game_is_on
    if flag > 5:
        game_is_on = False
    player2_paddle.goto(330,0)
    player1_paddle.goto(-335,0) 
    pingpong.timespeed = 0.1
    screen.update()
    time.sleep(0.5)
    
    

#Screen setup
screen = Screen()
screen.setup(700,600)
screen.title('Ping pong game')
screen.bgcolor('black')
screen.tracer(0)

score = Scoreboard()
player1_paddle = Paddle()
player1_paddle.goto(-335,0)         
player2_paddle = Paddle()
player2_paddle.goto(330,0)
pingpong = PingPong() 

middle_part = Turtle()
middle_part.color('white')
middle_part.penup()
middle_part.goto(0,-310)
middle_part.setheading(90)
while middle_part.ycor() <  310:
    middle_part.pendown()  
    middle_part.forward(30)
    middle_part.penup()
    middle_part.forward(30)

game_is_on = True
screen.listen()
screen.onkeypress(player1_paddle.south,'s')
screen.onkeypress(player1_paddle.north,'w') 
screen.onkeypress(player2_paddle.south,'Down')
screen.onkeypress(player2_paddle.north,'Up')

while game_is_on:

    time.sleep(pingpong.timespeed) 
    screen.update()
    pingpong.move()
    #collision with wall with player paddle
    player1_paddle.check_wall_collision()
    player2_paddle.check_wall_collision()

    
    if player2_paddle.distance(pingpong) < 50 and pingpong.xcor() > 325: 
        print('debug collided with 2nd paddle') 
        pingpong.xcordinate_increase *= -1
        #increase speed here
        pingpong.reduce_time()
        
    # checking if scored
    if pingpong.xcor() > 345:
        score2 = score.one_scored()
        pingpong.goto(0,0)
        refresh(score2)
        
    elif pingpong.xcor() < -345:
        score2 = score.two_scored()   
        pingpong.goto(0,0)
        refresh(score2)
        
        
    if player1_paddle.distance(pingpong) < 50 and   pingpong.xcor() < -325:
        print('debug collided with 1nd paddle')
        pingpong.xcordinate_increase *= -1
        #increase speed here
        pingpong.reduce_time()


    
    
    pingpong.collision_with_botom()
    pingpong.collision_with_top()

    
    

screen.exitonclick()
