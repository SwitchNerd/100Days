from turtle import Turtle, Screen
import random

#Create snake body
#Move the snake
#Control the snake
#Detect collision with food
#Create a scoreboard
#Detect collision with walls
#Detect collision with tail

scren = Screen()
scren.setup(600,600)
scren.bgcolor('black')
scren.title('Play Snake')
score = 0 
snake_body = []
scren.tracer(0,0)

for i in range(1,4):
    snake = Turtle()
    snake.penup()
    snake.color('white')
    snake.shape('square')
    xcor = snake.xcor()
    snake.goto(xcor - (i*20),0)
  
    snake_body.append(snake)

scren.update()
#snake_body[0].forward(20)
#scren.update()|


while True:
    
    for snakes in snake_body:
        #snakes.forward(70)]
        print(snakes.position())
        snakes.goto(0,0)
        scren.update()

    
    scren.exitonclick()