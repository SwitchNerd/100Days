from turtle import Turtle, Screen
import random

zaid_the_fatty = Turtle()
screen = Screen()
screen.setup(width=1500, height=900)
screen.screensize(1500,900)
colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0,90,180,270]
zaid_the_fatty.shape('classic') 
walk = 30
zaid_the_fatty.pensize(10)
zaid_the_fatty.speed(10)


for i in range(250):
    zaid_the_fatty.color(random.choice(colors))
    zaid_the_fatty.setheading(random.choice(directions))
    zaid_the_fatty.forward(walk)
    
    
screen.exitonclick()
