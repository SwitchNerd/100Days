from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)



zaid_the_fatty = Turtle()
screen = Screen()
screen.setup(width=1500, height=900)
screen.screensize(1500,900)
zaid_the_fatty.speed('fastest')

for i in range(1,37):
    my_tuple = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    zaid_the_fatty.circle(100)
    zaid_the_fatty.setheading(i*10)
    zaid_the_fatty.color(my_tuple)

screen.exitonclick()