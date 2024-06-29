COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.Turtles = []
        self.MOVE_INCREMENT = 10
        
    def create_cars(self):
        turtles = Turtle()
        turtles.turtlesize(1,2)
        turtles.shape('square')
        turtles.setheading(180)
        turtles.penup()
        ycords = random.randint(-250,250)
        turtles.color(random.choice(COLORS))
        turtles.goto(280,ycords)
        self.Turtles.append(turtles)
    
    def move(self):
        for turtles in self.Turtles:
            turtles.forward(STARTING_MOVE_DISTANCE)
    
    def check_distance(self,player):
        for turtles in self.Turtles:
            if turtles.distance(player) < 22:
                return True
            
    
    def new_level(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT