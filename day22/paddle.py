from turtle import Turtle



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 30
        self.color('white')
        self.shape('square')
        self.turtlesize(0.7,4)
        self.setheading(90)
        self.penup()
        
    
    def move(self):
        self.goto()
        
    def south(self):
        new_y = self.ycor() - self.move_speed
        self.sety(new_y)
    def north(self):
        new_y = self.ycor() + self.move_speed
        self.sety(new_y)
        
    def check_wall_collision(self):
         if self.ycor() <= -290:
             self.north()
         
         if self.ycor() >= 290:
             self.south()
    