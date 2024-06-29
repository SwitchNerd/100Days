from turtle import Turtle
import random

class PingPong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xcordinate_increase = 15
        self.ycordinate_increase=15
        self.timespeed = 0.1
    
    def move(self):
        self.goto(self.xcor() + self.xcordinate_increase , self.ycor() + self.ycordinate_increase)
        
    
    def collision_with_top(self):
        if self.ycor() >= 290:
            self.ycordinate_increase *= -1
            
    
    def collision_with_botom(self):
        if self.ycor() <= -290: 
            self.ycordinate_increase *= -1
    
    def reduce_time(self):
        self.timespeed *= 0.9