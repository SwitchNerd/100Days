STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        # Initalise the turtle
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)    
        self.shape('turtle')
    
    
    def move(self):
        self.forward(MOVE_DISTANCE)