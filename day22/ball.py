from turtle import Turtle
import random

class PingPong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = random.choice([-20,20])
        self.setheading(random.randint(0,90))
    
    def move(self):
        self.forward(self.move_speed)